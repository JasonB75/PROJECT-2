import socket
import json

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    send_dict = {"command": "kill", "volume":10, "type":"f", "precision":5}
    send_json = json.dumps(send_dict)
    send_byt = send_json.encode()
    s.connect((HOST, PORT))
    s.sendall(send_byt)
    data = s.recv(1024)

print(f"Received {data!r}")