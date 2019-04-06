import json
import os
import socket
from time import sleep

requests_to_server = [{'type': 4}, {'type': 3}, {'type': 2}, {'type': 1, "message": "hello world"}, {'type': 1},
                      {'type': 1, 'error_data': 'xD'}]


def request_to_server(request_to_parse):
    request_str = json.dumps(request_to_parse)
    request_bytes = str.encode(request_str)
    print('->', request_bytes)
    return request_bytes


config_file = "config/server_config.json"
if os.path.isfile(config_file):
    with open(config_file) as json_file:
        config_file = json.load(json_file)
        IP_ADDRESS = config_file['ipAddress']
        PORT_NUMBER = config_file['portNumber']

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (IP_ADDRESS, PORT_NUMBER)
print(f'connecting to {IP_ADDRESS} port {PORT_NUMBER}')
sock.connect(server_address)

for request in requests_to_server:
    sock.send(request_to_server(request))
    print('<-', sock.recv(1024))
    sleep(2);

request_bytes = b'bad encode data'
print('->', request_bytes)
sock.send(request_bytes)
print('<-', sock.recv(1024))

sock.close()
