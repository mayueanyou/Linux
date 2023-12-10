import os,sys,socket,threading,argparse

class Tcp_Server:
    def __init__(self, port, ip=None, call_back = None, call_back_arg = None) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        ip = socket.gethostbyname(socket.gethostname() if ip == None else ip
        self.server_address = (ip), port)
        print('starting server up on {} port {}'.format(*self.server_address))
        self.sock.bind(self.server_address)
        self.sock.listen()
        self.connection_list = []
        self.client_address_list = []
        self.call_back = self.echo_back if call_back==None else call_back
        self.accept_call(call_back_arg)
    
    def __del__(self):
        print('closing up on {} port {}'.format(*self.server_address))
        self.sock.close()
    
    def accept_call(self,call_back_arg):
        while True:
            connection, client_address = self.sock.accept()
            threading._start_new_thread(self.call_back,(connection,client_address,call_back_arg))
            
    def echo_back(self, connection, client_address, call_back_arg, buffer_size = 2048):
        try:
            print('connection from', client_address)
            while True:
                data = connection.recv(buffer_size)
                if data: connection.sendall(data)
        finally:
            print('connection clsoed', client_address)
            connection.close()
        
class Tcp_Client:
    def __init__(self, ip, port) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (ip, port)
        print('starting client connecting to {} port {}'.format(*self.server_address))
        self.sock.connect(self.server_address)
        
    def __del__(self):
        print('closing up on {} port {}'.format(*self.server_address))
        self.sock.close()
    
    def echo_back(self, message='Hello'):
        try:
            self.send_data(message)
            data = self.receive_data(len(message))
            print(f'received {str(data, encoding="utf-8")}')

        finally:
            print('closing socket', self.server_address)
            self.sock.close()
    
    def send_data(self,data):
        data = bytes(data, encoding='utf-8')
        self.sock.sendall(data)
    
    def receive_data(self,length):
        data = self.sock.recv(length)
        return data
    
    def receive_data_backup(self,length):
        amount_received = 0
        data = ''
        while amount_received < length:
            data += self.sock.recv(16)
            amount_received += len(data)
        return data 

def server():
    server = Tcp_Server(5000)

def clent():
    client = Tcp_Client('128.230.21.183', 5000)
    client.echo_back('asdfasdfjkaddasfasdfkldjasflasf')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--function', type=str)
    args = parser.parse_args()
    getattr(sys.modules[__name__], args.function)()
