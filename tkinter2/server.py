import socket
import threading

class server:
    def __init__(self):
        self.socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connections=[]
        self.send=True
        self.lock=threading.Lock()
        self.dict={}
        self.socket.bind(('0.0.0.0',5000))
        self.socket.listen(10)
    def handel(self,c,a):
        while True:
            self.lock.acquire()
            try:
                data=c.recv(1024)
                if self.send:
                    for client in self.connections:
                        client.send(data)
                    if not data:
                        print('<',str(a),'>','disconnect')
                        self.connections.remove(c)
                        c.close()
                self.lock.release()
            except:
                self.connections.remove(c)
                c.close()
                print('<',str(a),'>','disconnect')
                self.lock.release()
    def run(self):
        while True:
            self.lock.acquire()
            c,a=self.socket.accept()
            if a[0]=='127.0.0.1':
                cthread=threading.Thread(target=self.handel,args=(c,a))
                cthread.daemon=True
                self.connections.append(c)
                self.dict[c]=a[0]
                print(self.connections)
                cthread.start()
                print('<',str(a),'>','connect')
            else:
                self.send=False
                for client in self.dict:
                    if self.dict[client]=='127.0.0.1':
                        client.send('salam')
                        print(client.recv(1024))
            self.lock.release()
                
server=server()
server.run()
