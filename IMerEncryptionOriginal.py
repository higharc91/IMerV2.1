##this is going to be my Encrypt/Decrypt class##
##To parameters are needed. the message, and the passphrase##
###This is going to be based on a symetric XOR cipher scheme###
import binascii, re
global passPhrase, mess

def main(password,message):
    global passPhrase, mess
    passPhase = password
    mess = message
    #This function assigns the password to global var
    passPhrase = password
    encStart = IMer_Encryption()
    encStart.IMencrypt()


class IMer_Encryption():

    def __init__(self):
        self.cipherText = ""

    def IMencrypt(self,mess):
        binaryList = ""
        for i in mess:
            if i == " ":
                binaryList += "00100000"  #adding binary for space
            else:
                tmp = bin(int(binascii.hexlify(i),16)) #Binary Conversion
                newtemp = tmp.replace('b','') #This replaces python's method removes 'b' in the binary
                binaryList += newtemp
        return binaryList


    def IMpassEnc(self,password):
        binaryList = ""
        for i in password:
            if i == " ":
                binaryList += "00100000"  #adding binary for space
            else:
                tmp = bin(int(binascii.hexlify(i),16)) #Binary Conversion
                newtemp = tmp.replace('b','') #This replaces python's method removes 'b' in the binary
                binaryList += newtemp
        return binaryList

    def XOR(self,mess,password):
        #this takes the password and XORs the message and returns the cipher

        #this generates the variables for the XOR
        #--
        self.mess = self.IMencrypt(mess)
        self.passphrase = self.IMpassEnc(password)
        number = 0
        for i in self.mess:
            if i == ".":
                self.cipherText += ' '

            else:
                try:
                    if i == '0' and self.passphrase[number] == '0': #XOR table
                        self.cipherText += '0' #fix
                    elif i == '0' and self.passphrase[number] == '1':
                        self.cipherText += "1"
                    elif i == '1' and self.passphrase[number] == '0':
                        self.cipherText += "1"
                    elif i == '1' and self.passphrase[number] == '1':
                        self.cipherText += "0"
                except IndexError:
                    pass
                number += 1
        return self.cipherText

    def deEncrypt(self, ciphertext, passphrase):
        binarymessage, number = '', 0
        binaryList = ciphertext
        for i in binaryList:
                if i == ' ':
                    binarymessage += ' '
                else:
                    try:
                        if i == '0' and passphrase[number] == '0':
                            binarymessage += '0'
                        elif i == '0' and passphrase[number] == '1':
                            binarymessage += '1'
                        elif i == '1' and passphrase[number] == '0':
                            binarymessage += '1'
                        elif i == '1' and passphrase[number] == '1':
                            binarymessage += '0'
                        number += 1
                    except IndexError:
                        pass
        #hex1 = (''.join([chr(int(x,2)) for x in re.split('(........)', binarymessage) if x ])).decode('utf-8')
        return binarymessage

#test = IMer_Encryption()

#test.XOR("test this shit man","password")

#print test.IMpassEnc('password')

#test.deEncrypt()