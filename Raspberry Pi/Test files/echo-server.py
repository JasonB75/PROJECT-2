import socket
import json

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
the_earth_isnt_flat = True

while the_earth_isnt_flat:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                
                if not data:
                    break
                input_dict = json.loads(data.decode())
                if input_dict["command"] == "kill":
                    the_earth_isnt_flat = False
                    break
                else:
                    print(input_dict)
                output_dict = {"output": [11,1,1,1,2,2,1,1]}
                output_json = json.dumps(output_dict)
                out_byt = output_json.encode()
                conn.sendall(out_byt)