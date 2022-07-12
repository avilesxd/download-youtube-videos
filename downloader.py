from pytube import YouTube
from tkinter import *


def actions():
    link = videos.get()
    video = YouTube(link)
    descarga = video.streams.get_highest_resolution()
    descarga.download()


root = Tk()
root.config(bd=25)
root.resizable(0, 0)
root.title("Download videos")


instructionText = Label(
    root, text="enter the link of the video to download\n")
instructionText.grid(row=0, column=1)

videos = Entry(root)
videos.grid(row=1, column=1)

boton = Button(root, text="Download", command=actions)
boton.grid(row=2, column=1)

root.mainloop()
