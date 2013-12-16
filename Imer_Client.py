##This is the actual IM_Client handler..
"""In future releases I hope this will be in a gui
    however, atm it is just the framework"""

import socket, threading, time

class IM_Client():

    def __init__(self):
        self.userName = ""
        self.client = socket.socket()
        ##There needs to be the server determined ip here

    def __call__(self):
        return self   #THis is what you need to call

    def login(self, Servip):
        print("Welcome to Imer")
        print("wrote by HighArc")
        print("----------------\n \n")
        self.userName = raw_input("Enter your username: ")
        print("Establishing Connection..")
        time.sleep(3)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_addr =(Servip, 11117)
        self.client.connect(server_addr)
        time.sleep(1)
        threading.Thread(target=self.listener, args=()).start() #starts the listener
        self.client.send("%s joined the room.\n" % self.userName)
        #self.Imer()
        threading.Thread(target=self.Imer, args=()).start()

    def listener(self):
        while True:
            data = self.client.recv(1024)
            print (data)

    def Imer(self):
        while True:
            message =raw_input(" --> ")
            self.client.send(self.userName + ": "+ message)
