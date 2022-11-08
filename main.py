from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import psutil
import shutil
import os
import ctypes

#==Disk properties==#
listOfDisk = []
psutilDiskList = psutil.disk_partitions()
for disk in psutilDiskList:
	diskSpace = shutil.disk_usage(disk.device)
	diskProperties = [
		"Disk Name: "+disk.device[:-2],
		"File System Type: "+disk.fstype,
		"Mount Options: "+disk.opts,
		"Total: "+"{:.2f}".format(diskSpace.total/(2**30))+" GB",
		"Used: "+"{:.2f}".format(diskSpace.used/(2**30))+" GB",
		"Free: "+"{:.2f}".format(diskSpace.free/(2**30))+" GB"
		]
	listOfDisk.append(diskProperties)

#==Create window==#
root=Tk()
root.title("Memory Management")
root.geometry("600x400")

#==='General' tab===#
tabControl = ttk.Notebook(root)
tab1 = Frame(tabControl)
tabControl.add(tab1, text="General")

#====Update percentage bar====#
def updatePercentageBar(value, barPosX, basPosY, barLength):
	ttk.Progressbar(tab1, orient=HORIZONTAL, length=barLength, mode='determinate', value=value).place(x=barPosX+40, y=basPosY+6, height=10)
	labelText = StringVar()
	labelText.set("{:.1f}".format(value) + "%  ")
	Label(tab1, textvariable=labelText).place(x=barLength+70, y=basPosY)

#====Loop====#
def checkcpuram():
	updatePercentageBar(psutil.cpu_percent(), 20, 20, 300)
	updatePercentageBar(psutil.virtual_memory().percent, 20, 40, 300)
	root.after(1000, checkcpuram)

Label(tab1, text="CPU:").place(x=20, y=20)
Label(tab1, text="RAM:").place(x=20, y=40)

#==='Disk Properties' tab===#
tab2 = Frame(tabControl)
tabControl.add(tab2, text="Disk Properties")
posX=20
posY=10

#====Open 'Disk Properties' window====#
def viewDiskProperties(diskNo):
	newWindow = Toplevel(root)
	newWindow.title("Disk Properties")
	newWindow.geometry("300x200")
	newWindow.resizable(False, False)
	for i in range(3):
		Label(newWindow, text=listOfDisk[diskNo][i]).place(x=10, y=10+i*20)
	Label(newWindow, text="Disk Space:").place(x=10, y=70)
	for i in range(3,6):
		Label(newWindow, text=listOfDisk[diskNo][i]).place(x=20, y=30+i*20)

#====Defragment====#
def is_admin():
	try:
		return ctypes.windll.shell32.IsUserAnAdmin()
	except:
		return False

def defrag(diskName):
	if is_admin():
		messagebox.showinfo(title="Error", message="You need to be admin to perform this action")
	else:
		ctypes.windll.shell32.ShellExecuteW(None, "runas", 'powershell.exe', f"defrag {diskName}: /u /v", None, 1)

#====Add 'Properties' and 'Defragment' buttons====#
def placeButton(i):
	Button(tab2, text="Properties", command=lambda: viewDiskProperties(i)).place(x=posX+150, y=posY+i*30)
	Button(tab2, text="Defragment", command=lambda: defrag(listOfDisk[i][0][11:])).place(x=posX+230, y=posY+i*30)

for i in range(len(listOfDisk)):
	Label(tab2, text=listOfDisk[i][0][:4]+listOfDisk[i][0][10:]).place(x=posX, y=posY+i*30+4)
	placeButton(i)

#====Clean Disks====#
Button(tab2, text="Clean Disks", command=lambda: os.popen('Cleanmgr.exe / sagerun:1').read()).place(x=posX, y=posY+len(listOfDisk)*30+20)

#==Main==#
# Insert tabs
tabControl.pack(expand=1, fill=BOTH)
# Run Loop
checkcpuram()
# Run GUI
root.mainloop()