from tkinter import *
from tkinter import ttk
import psutil
from disk import Disk

from tkinter import messagebox

disk1 = Disk()

win=Tk()
win.title("Memory Management")
win.geometry("600x400")

def updatePercentageBar(value, barPosX, basPosY, barLength):
	ttk.Progressbar(win, orient=HORIZONTAL, length=barLength, mode='determinate', value=value).place(x=barPosX+40, y=basPosY+6, height=10)
	labelText = StringVar()
	labelText.set("{:.1f}".format(value) + "%  ")
	Label(win, textvariable=labelText).place(x=barLength+50, y=basPosY)
def checkcpuram():
	updatePercentageBar(psutil.cpu_percent(), 0, 0, 300)
	updatePercentageBar(psutil.virtual_memory().percent, 0, 20, 300)
	win.after(1000, checkcpuram)
def test():
	Label(win, text="CPU:").place(x=0, y=0)
	Label(win, text="RAM:").place(x=0, y=20)
	checkcpuram()

## View all the disks
view_All_Of_DiskPartitions_button = Button(text="View all the disks", width=13, command=disk1.view_All_Of_DiskPartitions)
view_All_Of_DiskPartitions_button.grid(row=1, column=1)


## view_Space_of_Disk
disk1.tao()
a = Button(text="View space", width=13, command=disk1.view_Space_of_Disk)
a.grid(row=3, column=5)

## Display cpu and ram usage
a = Button(text="Display cpu and ram usage", width=30, command=test)
a.grid(row=5, column=5)

## cleaning
a = Button(text="cleaning", width=30, command=disk1.cleaning)
a.grid(row=7, column=5)

## defragmentation
a = Button(text="defrag", width=30, command=disk1.defrag)
a.grid(row=8, column=5)



win.mainloop()