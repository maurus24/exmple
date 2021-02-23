from tkinter import *
from pytube import *
root = Tk()
root.geometry('500x400')
root.resizable(0,0)
root.title("Youtube vedio downloader")
Label(root,text='Youtube Vedio Downloader',font='arial 20 bold').pack()
link = StringVar()
Label(root,text='Paste Link Here:',font='arial 15 bold').place(x=160,y=60)
link_enter = Entry(root,width = 70,textvariable = link).place(x=32,y=90)
x = StringVar()
Label(root,text='Choose Resolution:',font='arial 15 bold').place(x=160,y=120)
x_enter = Entry(root,width = 70,textvariable = str(x)).place(x = 32,y=150)
def Showresolution():
    yt = YouTube(str(link.get()))
    liss = yt.streams.filter(progressive=True)
    for i in liss:
        print(i)
def Downloader():
    YouTube(str(link.get())).streams.filter(res=str(x.get())).first().download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 340 , y = 240)
def Audioonly():
    yt = YouTube(str(link.get()))
    yt.streams.filter(only_audio=True,file_extension='mp4').first().download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15',fg='green').place(x= 340 , y = 310)
Button(root,text = 'CHECK RESOLUTION AVAILABLE', font = 'arial 15 bold' ,bg = 'blue', padx = 2, command = Showresolution).place(x=90 ,y = 180)
Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=40 ,y = 240)
Button(root,text = 'DOWNLOAD(Audio only)', font = 'arial 15 bold' ,bg = 'orange', padx = 2, command = Audioonly).place(x=40 ,y = 310)

root.mainloop()
