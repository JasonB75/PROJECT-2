## request data paramiters
## type: binary or float
## quantity: how many data points i.e. how many binary bits or number of floats
## format: save to file, or output to commandline
## path: optional, if saving to file a path/filename

##public funtioncall, or request for command walkthrough

from persistqueue import Queue
import random
import json
import socket
import sys
import serial
from threading import Event, Thread
import time

#Setting up the persistQueue that will hold out data
PATH = "rad_bit_path6"
random_bit_q = Queue(PATH)

teensy_thread_stop_condition = Event()


HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)


def test_input(volume):
    for i in range(volume):
        random_bit_q.put(random.randint(0,1))
        #time.sleep(0.001)


#Converts a binary sequence into a floating point number between 0 and 1
#Assumes that the binary string is a binary fraction. Ex. 1101 assumes 0.1101
#Max realistic precision of 14 due to python's float var
def binary_to_decimal(binary_sequence):
    output = 0.0
    for i, bit in enumerate(binary_sequence):
        output += int(bit) * (2 ** -(i + 1))
    return output


#Function to fetch n number of bits from the queue
#Out: int of length = volume(int) 
def get_bits(volume):
    output = ""
    if volume <= random_bit_q.qsize():
        for i in range(volume):
            temp = random_bit_q.get()
            #print(temp)
            output += str(temp)
    else:
        return -1

    return output


def generate_output(volume, type, precision=6):
    out_list = []
    if type == "b":
        temp = get_bits(volume)
        if temp != -1:
            out_list = list(temp)
        else:
            pass
            #TODO
    elif type == "f":
        for i in range(volume):
            temp = get_bits(precision)
            if temp != -1:
                out_list.append(binary_to_decimal(temp))
            else:
                pass
                #TODO
    return out_list

def teensy_loop_listener():
    print("teensy thread starting...")

    teensy_serial = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    teensy_serial.reset_input_buffer()

    while not teensy_thread_stop_condition.is_set():

        if teensy_serial.in_waiting > 0:
            line = int(teensy_serial.readline().decode('utf-8').rstrip())
            if line == "0" or line == "1":
                random_bit_q.put(line)
                print("In: " + str(line))
        time.sleep(0.00001)
    print("teensy thread ending...")



def tcp_loop_listener():
    the_earth_isnt_flat = True
    print("Output loop listener started...")

    while the_earth_isnt_flat:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            teensy_thread_stop_condition.set()
            try:
                with conn:
                    print(f"Connected by {addr}")
                    while True:
                        data = conn.recv(200)
                        
                        if not data:
                            break

                        input_dict = json.loads(data.decode())

                        if input_dict["command"] == "kill":
                            the_earth_isnt_flat = False
                            break

                        elif input_dict["command"] == "data":
                            volume = input_dict["volume"]
                            type = input_dict["type"]
                            
                            if type == "b":
                                preciscion = 1
                            else:
                                preciscion = input_dict["precision"]
                            
                            output_list = generate_output(volume, type, preciscion)
                            output_dict = {"output": output_list}
                            output_json = json.dumps(output_dict)
                            out_byt = output_json.encode()

                            print(sys.getsizeof(out_byt))
                            conn.sendall(out_byt)
                            print(random_bit_q.qsize())

                        else:
                            print(input_dict)

                        
            finally:
                print("Closing current connection")
                conn.close()
    print("Output loop listener Ending...")



def main():
    #test_input(50000)
    '''testbit = get_bits(5)
    print(testbit)
    print(binary_to_decimal(testbit))
    print("")

'''
    print("Starting up...")
    print(random_bit_q.qsize())
    #print(random_bit_q.get())
    #print(random_bit_q.get())
    #print(random_bit_q.get())
    #print(binary_to_decimal(get_bits(5)))
    teensy_thread = Thread(target=teensy_loop_listener, args=())
    #teensy_thread.daemon = True
    tcp_thread = Thread(target=tcp_loop_listener, args=())
    teensy_thread.start()
    tcp_thread.start()

    tcp_thread.join()
    
    teensy_thread_stop_condition.set()
    print("task done")
    random_bit_q.task_done()

if __name__ == "__main__":
    main()


