import socketserver

class MyHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while 1:
            dataReceived = self.request.recv(1024)
            if not dataReceived: break
            #self.request.send(dataReceived)
            print(dataReceived)

myServer = socketserver.TCPServer(('127.0.0.1', 2325), MyHandler)
myServer.serve_forever()
