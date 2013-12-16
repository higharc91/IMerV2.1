##this is going to be my Encrypt/Decrypt class##
##To parameters are needed. the message, and the passphrase##
###This is going to be based on a symetric XOR cipher scheme###
import binascii, re
global passPhrase

"""def main(password,message):
    global passPhrase, mess
    passPhase = password
    mess = message
    #This function assigns the password to global var
    passPhrase = password
    encStart = IMer_Encryption()
    encStart.IMencrypt() """


class IMer_Encryption():

    def __init__(self):
        self.cipherText = ""

    def IMencrypt(self,mess):
        binaryList = ""
        binaryList += ''.join(format(ord(i),'0>8b') for i in mess)
        return binaryList


    def IMpassEnc(self,password):
        binaryList = ""
        binaryList += ''.join(format(ord(i),'0>8b') for i in password)
        return binaryList

    def XOR(self,mess,password):
        #this takes the password and XORs the message and returns the cipher

        #this generates the variables for the XOR
        #--
        #NOTE going into here fine mess and pass + username
        self.mess = self.IMencrypt(mess)
        self.passphrase = self.IMpassEnc(password)
        number = 0
        length = 0
        length = len(self.passphrase)
        for i in self.mess:
            if i == ".":
                self.cipherText += ' '

            else:
                try:
                    if number == length:
                        number = 0
                        if i == '0' and self.passphrase[number] == '0': #XOR table
                            self.cipherText += '0' #fix
                        elif i == '0' and self.passphrase[number] == '1':
                            self.cipherText += "1"
                        elif i == '1' and self.passphrase[number] == '0':
                            self.cipherText += "1"
                        elif i == '1' and self.passphrase[number] == '1':
                            self.cipherText += "0"
                        number += 1
                    else:
                        if i == '0' and self.passphrase[number] == '0': #XOR table
                            self.cipherText += '0' #fix
                        elif i == '0' and self.passphrase[number] == '1':
                            self.cipherText += "1"
                        elif i == '1' and self.passphrase[number] == '0':
                            self.cipherText += "1"
                        elif i == '1' and self.passphrase[number] == '1':
                            self.cipherText += "0"
                        number += 1
                except IndexError:
                    pass
        value = self.cipherText
        self.cipherText = ""
        return value

    def deEncrypt(self, ciphertext, passphrase):
        binarymessage, number = '', 0
        binaryList = ciphertext
        length = len(passphrase)
        for i in binaryList:
            if i == ".":
                binarymessage += ' '

            else:
                try:
                    if number == length:
                        number = 0
                        if i == '0' and passphrase[number] == '0': #XOR table
                            binarymessage += '0' #fix
                        elif i == '0' and passphrase[number] == '1':
                            binarymessage += "1"
                        elif i == '1' and passphrase[number] == '0':
                            binarymessage += "1"
                        elif i == '1' and passphrase[number] == '1':
                            binarymessage += "0"
                        number += 1
                    else:
                        if i == '0' and passphrase[number] == '0': #XOR table
                            binarymessage += '0' #fix
                        elif i == '0' and passphrase[number] == '1':
                            binarymessage += "1"
                        elif i == '1' and passphrase[number] == '0':
                            binarymessage += "1"
                        elif i == '1' and passphrase[number] == '1':
                            binarymessage += "0"
                        number += 1
                except IndexError:
                    pass

        hex1 = (''.join([chr(int(x,2)) for x in re.split('(........)', binarymessage) if x ])).decode('utf-8')
        return hex1

#test = IMer_Encryption()

#print test.XOR("hi kiefer whats up","jarred")

#print test.IMpassEnc('hi kiefer whats up')
#messy = '0010100100001110000000000000000101010010010010010000000101011000'

#print test.deEncrypt(messy, "0111000001100001011100110111001101110111011011110111001001100100")

#print test.IMencrypt('test')
