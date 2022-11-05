import psutil
import shutil
import os
import time
from tkinter import *
from tkinter import messagebox
import ctypes, sys


class Disk():

    def __init__(self):
        self.flag = 0
        self.disk = ""
        self.listDisk = []

    def tao(self):
        self.space_entry1 = Entry(width=35)
        self.space_entry1.grid(row=3, column=1)
        self.space_entry1.insert(0, "Which disk do you want to view ?")
        self.space_entry1.focus()
        self.space_entry2 = Entry(width=35)
        self.space_entry2.grid(row=8, column=1)
        self.space_entry2.insert(0, "Which disk do you want to defrag ?")
        self.space_entry2.focus()

    def set_disk(self, x):
        self.disk = x

    ## View all of drive
    def view_All_Of_DiskPartitions(self):
        x = ""
        new_list = psutil.disk_partitions()
        for i in new_list:
            lst = list(i)
            print(lst[0][0:1])
            x += "Disk: " + lst[0][0:1] + " fstype: " + lst[2] + " opts: " + lst[3] + "\n"
            self.listDisk.append(lst[0][0:1])
        messagebox.showinfo("View", message=x)

    ## View space
    def view_Space_of_Disk(self):

        disk = self.space_entry1.get()
        if disk in self.listDisk:
            path = f"{disk}:/"
            ## them cho sua khong phai o dia
            total, used, free = shutil.disk_usage(path)
            x = ""
            x += "Total space: " + str(round(total / 2 ** 30)) + "GB\n"
            x += "Used space: " + str(round(used / 2 ** 30)) + "GB\n"
            x += "Free space: " + str(round(free / 2 ** 30)) + "GB\n"
            messagebox.showinfo(title="View space", message=x)
            if free <= total / 2:
                self.flag = 1
        else:
            messagebox.showinfo(title="Error", message="Khong tim thay o nay")

    ## cleaning
    def cleaning(self):
        clean = os.popen('Cleanmgr.exe / sagerun:1').read()
        defrag = os.popen('dfrgui.exe C: C/ F/ M')
        print(clean)

    def is_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def defrag(self):
        x = self.space_entry2.get()
        if x in self.listDisk:

            if self.is_admin():
                print("No")
            else:
                ctypes.windll.shell32.ShellExecuteW(None, "runas", 'powershell.exe', f"defrag {x}: /u /v", None, 1)
        else:
            messagebox.showinfo(title="Error", message="Khong tim thay o nay")