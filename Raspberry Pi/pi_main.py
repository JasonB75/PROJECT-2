## request data paramiters
## type: binary or float
## quantity: how many data points i.e. how many binary bits or number of floats
## format: save to file, or output to commandline
## path: optional, if saving to file a path/filename

##public funtioncall, or request for command walkthrough

from persistqueue import Queue
import random


PATH = "rad_bit_path2"
random_bit_q = Queue(PATH, autosave=True)


def test_input(volume):
    for i in range(volume):
        random_bit_q.put(random.randint(0,1))


#Converts a binary sequence into a floating point number between 0 and 1
#Assumes that the binary string is a binary fraction. Ex. 1101 assumes 0.1101
#Max realistic precision of 15 due to python's float var
def binary_to_decimal(binary_sequence):
    output = 0.0
    for i, bit in enumerate(binary_sequence):
        output += int(bit) * (2 ** -(i + 1))
    return output


#Function to fetch n number of bits from the queue
#Out: int of lengtg = volume(int) 
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


def main():
    test_input(500)
    '''testbit = get_bits(5)
    print(testbit)
    print(binary_to_decimal(testbit))
    print("")

'''
    print(random_bit_q.qsize())
    print(random_bit_q.get())
    print(random_bit_q.get())
    print(random_bit_q.get())
    print(binary_to_decimal(get_bits(5)))
    random_bit_q.task_done()

if __name__ == "__main__":
    main()
