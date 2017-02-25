import time
import webbrowser
import os
import tkMessageBox
i=1
path='C:\Users\LENOVO\Desktop\Udacity\Python'
file_list=os.listdir(path)
file=file_list[0]

while (i<4):
    print("Just wait for 2 hours. Do Your Job!")
    print("An alert sound will be played")

    time.sleep(2*60*60)
    os.startfile(path+"/"+file)
    tkMessageBox.showinfo(title="Alert", message="Stop Working! Relax Now!!")
    webbrowser.open("https://www.youtube.com/watch?v=xwtdhWltSIg")
    i=i+1
