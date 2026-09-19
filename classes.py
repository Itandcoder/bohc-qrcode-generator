from tkinter import *
from PIL import ImageTk, Image
import qrcode
import os




class Photo:
    def __init__(self,PhotoPath, PhotoSize):
        self.PhotoPath = PhotoPath
        self.PhotoSize = PhotoSize
    
    def imageResize(self):
        getImage = Image.open(self.PhotoPath)
        newImage = ImageTk.PhotoImage(getImage.resize(self.PhotoSize))
        return newImage




class QRC:
    def __init__(self, email, subject, body):
        self.email = email
        self.subject = subject
        self.body = body
    
    def newEmailQRCode(self):
        folder_name = r"./QRC"
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)

        img = qrcode.make(f"mailto:{self.email}?subject={self.subject}&body={self.body}")
        img.save("./QRC/newqrc.png")
        global newImage
        newImage = Photo("./QRC/newqrc.png", (400, 400)).imageResize()
        return newImage
        
    @staticmethod    
    def newURLQRCode(url):
        folder_name = r"./QRC"
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)

        img = qrcode.make(f"{url}")
        img.save("./QRC/newqrc.png")
        global newImage
        newImage = Photo("./QRC/newqrc.png", (400, 400)).imageResize()
        return newImage

        