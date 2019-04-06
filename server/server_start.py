from server.lib.network_interface import *
import server.lib.request_handler as req

if __name__ == "__main__":
    __testChain = req.EchoRequestHandler(req.PingRequestHandler(req.ServerListRequestHandler()))
    __server = Server(__testChain)
