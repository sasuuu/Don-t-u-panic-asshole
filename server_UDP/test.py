import socket
import time
import json
import pickle

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(6)

message = {
    "auth_key": "abc",
    "type": "1",
    "data": ["nick"]
}
msg = pickle.dumps(json.dumps(message))
addr = ("127.0.0.1", 7070)

client_socket.sendto(msg, addr)
data, server = client_socket.recvfrom(4096)
print(data)
data, server = client_socket.recvfrom(4096)
print(data)
