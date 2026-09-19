from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from classes import Photo, QRC
from tkinter import filedialog




# Main Window
root = Tk()
root.geometry("1200x800")
root.maxsize(1200, 800)
root.config(bg="#95989c")
root.title("QRCode Generator")
icon_image = PhotoImage("./pngqrlogo.png")
root.iconphoto(True, icon_image)
#root.iconbitmap("./images/icoqrlogo.ico")
qrcodeLogo = Photo("./images/qrlogo.png", (405, 405)).imageResize()

# Heading Frame
headingFrame = Frame(root, bg="#95989c")
headingFrame.pack(pady=10)
appTitle = Label(headingFrame, text="QR  Code  Generator", bg="#95989c", font=("Times", 30))
appTitle.grid(column=0, row=0, padx=300)
companyLogo = Photo("./images/bohclogo.png", (130, 80)).imageResize()
companyLogoLabel = Label(headingFrame, image=companyLogo)
companyLogoLabel.grid(column=1, row=0)

# Main Frame
mainFrame = Frame(root, bg="#b8b8b8")
mainFrame.pack(padx=20)

# Label Frames
emailLabelFrame = LabelFrame(mainFrame, text="QR Code for Email", bg="#b8b8b8")
emailLabelFrame.grid(column=0, row=0, padx=10, pady=10)
urlLabelFrame = LabelFrame(mainFrame, text="QR Code for URL", bg="#b8b8b8")
urlLabelFrame.grid(column=0, row=1, padx=10, pady=10, columnspan=2)
qrcodeLabelFrame = LabelFrame(mainFrame, text="QR Code", bg="#b8b8b8")
qrcodeLabelFrame.grid(column=1, row=0, padx=10, pady=10)

# App Logo
qrcodeDisplay = Label(qrcodeLabelFrame, image=qrcodeLogo)
qrcodeDisplay.grid(column=0, row=0)

# Label and Entry
# Email
labelEmail = Label(emailLabelFrame, text="Email", bg="#b8b8b8")
labelEmail.grid(column=0, row=0, padx=10, sticky=W)
entryEmail = Entry(emailLabelFrame, bg="#232324", fg="#0ff21e", width=50)
entryEmail.grid(column=0, row=1, padx=10, sticky=W)
entryEmail.focus()

# Subject
labelSubject = Label(emailLabelFrame, text="Subject:", bg="#b8b8b8")
labelSubject.grid(column=0, row=2, padx=10, sticky=W)
entrySubject = Entry(emailLabelFrame, bg="#232324", fg="#0ff21e", width=107)
entrySubject.grid(column=0, row=3, padx=10, sticky=W)

# Body
labelBody = Label(emailLabelFrame, text="Body:", bg="#b8b8b8")
labelBody.grid(column=0, row=4, padx=10, sticky=W)
entryBody = Text(emailLabelFrame, bg="#232324", fg="#0ff21e", height=19)
entryBody.grid(column=0, row=5, padx=10)

# URL
labelUrl = Label(urlLabelFrame, text="URL from website:", bg="#b8b8b8")
labelUrl.grid(column=0, row=0, padx=10, sticky=W)
entryUrl = Entry(urlLabelFrame, bg="#232324", fg="#0ff21e", width=180)
entryUrl.grid(column=0, row=1, padx=10, sticky=W)




# Functions for Buttons
def resetData():
    entryEmail.delete(0, END)
    entrySubject.delete(0, END)
    entryBody.delete("1.0", "end-1c")
    entryUrl.delete(0, END)
    qrcodeDisplay.configure(image=qrcodeLogo)

def generateEmailQRCode():
    entryUrl.delete(0, END)
    txtEmail = entryEmail.get()
    txtSubject = entrySubject.get()
    txtBody = entryBody.get("1.0", "end-1c")
    if len(txtEmail) > 0 and len(txtSubject) > 0 and len(txtBody) > 0:
        newImage = QRC(txtEmail, txtSubject, txtBody).newEmailQRCode()
        qrcodeDisplay.configure(image=newImage)
        entryEmail.focus()
    else:
        messagebox.showinfo("Notification", "All email fields are required.")

def generateURLQRCode():
    entryEmail.delete(0, END)
    entrySubject.delete(0, END)
    entryBody.delete("1.0", "end-1c")
    txtURL = entryUrl.get()
    if len(txtURL) > 0:
        newImage = QRC.newURLQRCode(txtURL)
        qrcodeDisplay.configure(image=newImage)
    else:
        messagebox.showinfo("Notification", "Url field is required.")

def saveImage():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")])
    if file_path:
        try:
            img = Image.open("./QRC/newqrc.png")
            img.save(file_path)
            resetData()
        except:
            pass




# Buttons
buttonGenerateEmailQRCode = Button(emailLabelFrame, text="Generate", bg="#b8b8b8", width=10, height=1, command=generateEmailQRCode)
buttonGenerateEmailQRCode.grid(column=0, row=6, pady=20)
buttonGenerateURLQRCode = Button(urlLabelFrame, text="Generate", bg="#b8b8b8", width=10, height=1, command=generateURLQRCode)
buttonGenerateURLQRCode.grid(column=0, row=6, pady=20)
buttonSave = Button(qrcodeLabelFrame, text="Save", bg="#b8b8b8", width=10, height=1, command=saveImage)
buttonSave.grid(column=0, row=1, pady=20)




# Events
# Entry Email Event & Bind
def entryEmailFocusIn(event):
    entryEmail.configure(background="#5c5c5c")
def entryEmailFocusOut(event):
    entryEmail.configure(background="#232324")
entryEmail.bind('<FocusIn>', entryEmailFocusIn)
entryEmail.bind('<FocusOut>', entryEmailFocusOut)

# Entry Subject Event & Bind
def entrySubjectFocusIn(event):
    entrySubject.configure(background="#5c5c5c")
def entrySubjectFocusOut(event):
    entrySubject.configure(background="#232324")    
entrySubject.bind('<FocusIn>', entrySubjectFocusIn)
entrySubject.bind('<FocusOut>', entrySubjectFocusOut)

# Entry Body Event & Bind
def entryBodyFocusIn(event):
    entryBody.configure(background="#5c5c5c")
def entryBodyFocusOut(event):
    entryBody.configure(background="#232324")    
entryBody.bind('<FocusIn>', entryBodyFocusIn)
entryBody.bind('<FocusOut>', entryBodyFocusOut)

# Entry URL Event & Bind
def entryURLFocusIn(event):
    entryUrl.configure(background="#5c5c5c")
def entryURLFocusOut(event):
    entryUrl.configure(background="#232324")    
entryUrl.bind('<FocusIn>', entryURLFocusIn)
entryUrl.bind('<FocusOut>', entryURLFocusOut)

# Button Email Event & Bind
def buttonEmailEnter(event):
    buttonGenerateEmailQRCode.configure(bg="#0ff21e")
def buttonEmailLeave(event):
    buttonGenerateEmailQRCode.configure(bg="#b8b8b8")
buttonGenerateEmailQRCode.bind('<Enter>', buttonEmailEnter)
buttonGenerateEmailQRCode.bind('<Leave>', buttonEmailLeave)

# Button URL Event & Bind
def buttonURLEnter(event):
    buttonGenerateURLQRCode.configure(bg="#0ff21e")
def buttonURLLeave(event):
    buttonGenerateURLQRCode.configure(bg="#b8b8b8")
buttonGenerateURLQRCode.bind('<Enter>', buttonURLEnter)
buttonGenerateURLQRCode.bind('<Leave>', buttonURLLeave)

# Button Save Event & Bind
def buttonSaveEnter(event):
    buttonSave.configure(bg="#0ff21e")
def buttonSaveLeave(event):
    buttonSave.configure(bg="#b8b8b8")
buttonSave.bind('<Enter>', buttonSaveEnter)
buttonSave.bind('<Leave>', buttonSaveLeave)




Label(root, text="IT Department, Best Option Healthcare.     - QR Code Generator 10.6.25 -     by Roberto J. Alvarez", bg="#95989c").pack(pady=10)



root.mainloop()