"""This programs is an expansion of the IMerMain Program.
It's purpose is to look on the selected network range for
a host that is listening on the Imer port 11117 and return
the value back to Imer."""

import socket, time
import re

def find(ip):  #this needs to have the input for ip
    print("Looking for any running IM servers")
    time.sleep(2)
    ip2 = re.split(r'(\.|)', ip)
    newIP = ""
    newIP= ''.join(ip2[0:-1])
    for i in range(0,254):
       s = socket.socket(socket.AF_INET, socket. SOCK_STREAM)  #this had to be moved here, must be reopened
       s.settimeout(0.1)
       sockIp = ""
       sockIp = str((newIP+ str(i)))
       response = s.connect_ex((sockIp, 11117))
       if response:
           print("Server not found on %s" % sockIp)
           s.close()

#lint:disable

       else:
           print("Server found on %s Now connecting to current IM session" % sockIp)
           s.close()
           time.sleep(3)
           return sockIp
       #except socket.error:        #need to figure out how to take the connection trigger and show it
        #   print("failed on %s" % sockIp)


