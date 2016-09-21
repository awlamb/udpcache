from socketserver import BaseRequestHandler, UDPServer
from stack import Stack

class UDPHandler(BaseRequestHandler):
    stack = Stack()
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        self.parse(socket,data)
        socket.sendto(data.upper(),self.client_address)

    def parse(self,socket, command):
        command = command.decode('utf-8').split(' ')
        if command[0] == 'push':
            self.stack.add(command[1],command[2])
        if command[0] == 'pop':
            pop_value = self.stack.pop(command[1])
            if pop_value:
                socket.sendto(bytes(pop_value,'utf-8'), self.client_address)
            else:
                socket.sendto(bytes('none','utf-8'), self.client_address)

if __name__ == "__main__":
    HOST,PORT = "localhost", 9999
    server = UDPServer((HOST,PORT), UDPHandler)
    server.serve_forever()

