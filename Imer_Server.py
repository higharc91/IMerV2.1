import socket, threading, time


class IM_Server():
    """The main goal is to call this class when IMER can not
       a current active server, thus making one locally"""
    def __init__(self):
        self.clientlist = [] #stores client connections
        self.sockserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #tcp conn init
        self.sockserver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) #closes port when done

    def __call__(self):
        return self   #THis is what you need to call

    def listen(self, ip):
        self.sockserver.bind((ip, 11117))
        self.sockserver.listen(5)
        print('Server started on %s' %ip)
        while True:
            try:
                client, addr = self.sockserver.accept()
                self.clientlist.append(client)
                print('client Connected:', client.getpeername())  #all these added prints remove
                threading.Thread(target=self.handler, args=(client,)).start()
            except:
                continue

    def handler(self,client):
        while True:
            try:
                data = client.recv(1024)
                if data:  #checks to see if there is data
                    threading.Thread(target=self.responder, args=(data,)).start()
                else:
                    continue
            except:
                pass
    def responder(self,data):
        for c in self.clientlist:
            try:
                c.send(data)
            except:
                self.clientlist.remove(c)
                continue


