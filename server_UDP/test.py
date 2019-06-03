import socket
import time
import json
import pickle

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1.0)

message = {
    "auth_key": "abc"
}
msg = pickle.dumps(json.dumps(message))
addr = ("127.0.0.1", 7070)

client_socket.sendto(msg, addr)
time.sleep(2)
client_socket.sendto(msg, addr)
