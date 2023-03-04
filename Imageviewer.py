import os
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox

root = Tk()
cwd=os.getcwd()
root.title(f"Imageviewer   Current Folder: [{cwd}]")
label1 = Label(root, text="Put this Application in a Folder Containing images to view them",font=("times new roman",11,"bold"))
label1.config(highlightthickness=0, highlightbackground="white", bg="light cyan")
label1.pack()
label3 = Label(root, text="Double click Next/Previous to start followed by single click or Use Arrow Keys < > ,  Esc to Exit",font=("times new roman",11,"bold"))
label3.config(highlightthickness=0, highlightbackground="white", bg="light cyan")
label3.pack()

root.minsize(1030,700)
root.maxsize(1050,750)
root['bg'] = 'light cyan'
folder_path=os.getcwd()
files = os.listdir(folder_path)
images=[]
formats=(".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg",".heif", ".psd",".ico")
image_files = [file for file in os.listdir() if file.endswith(formats)]

frame=Frame(root,bg="Light cyan",relief=SUNKEN)
frame.pack(side=BOTTOM,anchor="sw",padx=365,fill=Y)

#for getting assets from temp folder
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

root.wm_iconbitmap(resource_path("icon.ico"))

if not image_files:
    messagebox.showinfo("Information","Please place the Application inside a folder containing Images Ignore Any Traceback Errors. \nWhen Application is put in Folder containing large amount of Images, Just Wait for some time to open the App.")
    root.quit()
else:
    for file in files:
        if file.endswith(formats):
            # Open the image using the Image module of PIL
            image = Image.open(os.path.join(folder_path, file))
            # Resize the image to fit in the window
            image = image.resize((1030, 700))
            # Convert the image to a Tkinter-compatible format
            photo = ImageTk.PhotoImage(image)
            # Add the photo to the list of images
            images.append(photo)

# Create a label to display the photos
label = Label(root)

# Set the initial photo to display
current_image = 1
label.config(image=images[current_image])
label.pack()

# Create a function to cycle through the photos
def next_image(event=None):
        global current_image
        label.config(image=images[current_image])
        current_image = (current_image + 1) % len(images)
def prev_image(event=None):
    global current_image
    current_image = (current_image - 1) % len(images)
    label.config(image=images[current_image])
def exit(event=None):
    root.quit()
# Create a button to cycle through the photos

button1 = Button(frame, text="   Next  ->  ",borderwidth=4,background="white",activebackground="grey",activeforeground="white",font=('calibri 11 bold'), command=next_image)
button1.pack(side=LEFT,anchor="sw",padx=6,pady=8)
button2 = Button(frame, text=" <- Previous  ",borderwidth=4,background="White",activebackground="grey",activeforeground="white",font=('calibri 11 bold'), command=prev_image)
button2.pack(side=LEFT,padx=9,pady=8)
button3 = Button(frame,text="      Exit      ",borderwidth=4,background="white",activebackground="grey",activeforeground="white",font=('calibri 11 bold'),command=root.quit)
button3.pack(side=LEFT,padx=6,pady=8)

root.bind('<Right>',next_image)
root.bind('<Left>',prev_image)
root.bind('<Escape>',exit)

root.mainloop()