#! /usr/bin/env python
# -*- python -*-
# Generated by PAGE version 4.0.1
# In conjuction with Tcl version 8.6
#    Oct. 30, 2013 04:47:53 AM
import sys, IMerEncryption
import socket, threading, time
global value
global snt
global ent
ent = "0"
value = "0"
snt = False
py2 = py30 = py31 = False
version = sys.hexversion
if version >= 0x020600F0 and version < 0x03000000 :
    py2 = True    # Python 2.6 or 2.7
    from Tkinter import *
    import ttk
elif version >= 0x03000000 and version < 0x03010000 :
    py30 = True
    from tkinter import *
    import ttk
elif version >= 0x03010000:
    py31 = True
    from tkinter import *
    import tkinter.ttk as ttk
else:
    print ("""
    You do not have a version of python supporting ttk widgets..
    You need a version >= 2.6 to execute PAGE modules.
    """)
    sys.exit()



def vp_start_gui(servIp,passw):
    '''Starting point when module is the main routine.'''
    global val, w, root, start, ip, password
    password = passw
    ip =servIp
    value = 1
    root = Tk()
    root.title('IMer V2')
    root.geometry('600x450+650+150')

    w = New_Toplevel_1 (root)
    if value == 1:
        threading.Thread(target=handlerMain, args=()).start()
        value = 2
    #handlerMain()
    init()
    root.mainloop()

def handlerMain(): #this is the function to start the IM client
    start = IM_Client()
    start.login(ip)


w = None
def create_New_Toplevel_1 (root):
    '''Starting point when module is imported by another program.'''
    global w, w_win
    if w: # So we have only one instance of window.
        return
    w = Toplevel (root)
    w.title('New_Toplevel_1')
    w.geometry('600x450+650+150')
    w_win = New_Toplevel_1 (w)

    init()
    return w_win

def destroy_New_Toplevel_1 ():
    global w
    w.destroy()
    w = None




def init():
    pass




class New_Toplevel_1:
    def __init__(self, master=None):
        _bgcolor = 'SystemButtonFace'  # X11 color: #f0f0f0
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = 'SystemButtonFace' # X11 color: #f0f0f0
        _ana1color = 'SystemButtonFace' # X11 color: #f0f0f0
        _ana2color = 'SystemButtonFace' # X11 color: #f0f0f0
        TkFixedFont = "-family {Courier New} -size 10 -weight normal -slant roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])


        self.scrollbar = Scrollbar(master)
        self.scrollbar.place(relx=0.02,rely=0.2,relheight=0.63,relwidth=0.96)
        self.listbox = Listbox(master, yscrollcommand=self.scrollbar.set)
        self.listbox.place(relx=0.02,rely=0.2,relheight=0.63,relwidth=0.96)
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.configure(background="grey")
        self.listbox.configure(selectbackground="#00e963")



        self.Entry1 = Entry (master)
        self.Entry1.place(relx=0.02,rely=0.89,relheight=0.07,relwidth=0.84)
        self.Entry1.configure(background="grey")
        self.Entry1.configure(disabledforeground="#b4b4b4")
        self.Entry1.configure(font=TkFixedFont)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=504)

        self.Button1 = Button (master,command = self.button) #here is for the button
        self.Button1.place(relx=0.88,rely=0.88,height=34,width=57)
        self.Button1.configure(activeforeground="#00e963")
        self.Button1.configure(disabledforeground="#b4b4b4")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(borderwidth=2)
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Send''')
        self.Button1.configure(width=57)


        self.Canvas1 = Canvas (master)
        self.Canvas1.place(relx=0.02,rely=0.02,relheight=0.11,relwidth=0.80)
        self.Canvas1.configure(background="black")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="#d8d8d8")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(width=556)
        self.example_has_been_called = "0"  #bool created here

        #here comes the code for the Image title
        self.Canvas1.background = PhotoImage(file = 'lib/IMer2.gif')
        self.Canvas1.create_image(3,4,image= self.Canvas1.background, anchor=NW,)


        #app handler goes below---------#
        #start = IM_Client()
        #start.login("192.168.1.1")

    def button(self):
        global value #this returns the value
        #global snt
        value = "1"
        #snt = True
        self.click()


    def click(self):
        global value, snt
        # This checks for a entry and returns the value
        #these two bools only change if called
        if value == "0":  #keeps looping here..
                return "0"
        elif value == ("1"):
            #self.example_has_been_called = True
            self.EntryValue()
            snt = True
            #value = "0"
            return "1"

    def EntryValue(self):
        return self.Entry1.get()

#Here is the framework of the application

class IM_Client():

    def __init__(self):
        self.ENC = IMerEncryption.IMer_Encryption()
        self.Insert = New_Toplevel_1()
        self.userName = ""
        self.client = socket.socket()
        #self.GUIdis = New_Toplevel_1().Scrolledlistbox1()
        ##There needs to be the server determined ip here

    def __call__(self):
        return self   #THis is what you need to call

    def login(self, Servip):
        global value
        self.Insert.Entry1.focus() #setting focus for entry box
        #self.Insert = New_Toplevel_1()
        self.Insert.listbox.insert(END,"Welcome to Imer")
        self.Insert.listbox.insert(END,"wrote by HighArc")
        self.Insert.listbox.insert(END,"--------------------------")
        self.Insert.listbox.insert(END,"")
        self.Insert.listbox.insert(END,"Enter your username in the box below and click Send")
        name =  True
        while name == True:
            if value == "0":
                continue

            elif value == "1":
                self.userName =(self.Insert.EntryValue())
                if self.userName ==( None or "None"):
                    value = "0"
                    continue
                elif self.userName:
                    name = False
            else:
                continue
        #self.userName =(self.Insert.EntryValue())
        self.Insert.Entry1.delete(0, END)
        self.Insert.listbox.insert(END,"Establishing Connection.....")
        time.sleep(3)
        value = "0"  #this may need to be redefined
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_addr =(Servip, 11117)
        self.client.connect(server_addr)
        time.sleep(1)
        self.Insert.listbox.insert(END,("Signing in as %s" % self.userName))
        time.sleep(2)
        threading.Thread(target=self.listener, args=()).start() #starts the listener
        #self.client.send("%s joined the room." % self.userName)
        self.Imer()
        #threading.Thread(target=self.Imer, args=()).start()
    def listener(self):
        self.password = self.ENC.IMpassEnc(password)
        while True:
            self.data = self.client.recv(1024)
            decMess = self.ENC.deEncrypt(self.data,self.password)
            self.Insert.listbox.insert(END,decMess)
            decMess = ""
            self.Insert.listbox.yview(END) #this is added

                #except:
                    #pass


    def Imer(self):
        global snt
        snt = False
        while True:
            #w.Entry1.bind('<Return>', w.click())  #enter button bind   work on here!
            global value
            if snt == True:
                message = ""
                message =(self.Insert.EntryValue())  #checking for blank mess
                if message != "":
                    sendmess = self.ENC.XOR((self.userName + ": "+message),password)
                    self.client.send(sendmess)
                    sendmess = ""
                    snt = False
                    self.Insert.Entry1.delete(0, END)
                else:
                    continue

                snt = False


    def value(self):
        return self.Insert.click()


    #def click(self):
        #Return the entry when click


if __name__ == '__main__':
    vp_start_gui()


