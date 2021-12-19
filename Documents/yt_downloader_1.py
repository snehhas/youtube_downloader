import tkinter
from pytube import YouTube
import pytube
 
root = tkinter.Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Sneha's Youtube Video Downloader")

tkinter.Label(root, text ="Sneha's Youtube Downloader", font ='arial 20 bold').pack()

link = tkinter.StringVar()
 
tkinter.Label(root, text ='Paste Link Here:', font ='arial 15 bold').place(x= 160, y = 60)
link_enter = tkinter.Entry(root, width = 70, textvariable = link).place(x = 32, y = 90)


def Downloader():
    
    url =str(link.get())
    yt = pytube.YouTube(url)
    stream = yt.streams.get_highest_resolution()
    a=stream.download()
    tkinter.Label(root, text ="Yup, it's done Sneha !", font ='arial 15').place(x= 180, y = 210)
 
 
tkinter.Button(root, text ='DOWNLOAD', font ='arial 15', bg ='pink', padx = 2, command = Downloader).place(x=180, y = 150)
 
root.mainloop()

