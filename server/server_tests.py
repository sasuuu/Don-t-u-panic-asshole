# basic test client sending good and bad data

import json
import os
import socket
import pickle
from time import sleep

requests_to_server = [{'requestType': '3'}, {'requestType': '1', "message": "hello world"}, {'requestType': '1'},
                      {'requestType': '1', 'error_data': 'xD'}]

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
    to_send = pickle.dumps(json.dumps(request))
    sock.send(to_send)
    print('->', to_send)
    print('<-', json.loads(pickle.loads(sock.recv(262144))))
    sleep(1)

sock.close()
