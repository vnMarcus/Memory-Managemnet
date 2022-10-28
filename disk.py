import psutil
import  shutil
import  os
import time


class Disk():

    def __init__(self):
        self.flag = 0

    ## View all of drive
    def view_All_Of_DiskPartitions(self):
        new_list = psutil.disk_partitions()
        for i in new_list:
            lst = list(i)
            print("Disk: " + lst[0][0:1] + " fstype: " + lst[2] + " opts: " + lst[3])


    def view_Space_of_Disk(self):

        x = input("Which drive do you want to view")
        path = f"{x}:/"
        total, used, free = shutil.disk_usage(path)
        print("Total space: " + str(round(total / 2 ** 30)) + "GB")
        print("Used space: " + str(round(used / 2 ** 30)) + "GB")
        print("Free space: " + str(round(free / 2 ** 30)) + "GB")


        if free <= total / 2:
            self.flag = 1

    def cleaning(self):
        if self.flag == 1:
            clean = os.popen('Cleanmgr.exe / sagerun:1').read()
            defrag = os.popen('dfrgui.exe C: C/ F/ M')
            print(clean)


    def display_usage(self, cpu_usage, mem_usage, bars = 50):
        cpu_percent = (cpu_usage / 100.0)
        cpu_bar = '█' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))
        mem_percent = (mem_usage / 100.0)
        mem_bar = '█' * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))

        print(f"\r CPU usage: |{cpu_bar}| {cpu_usage:.2f}% ", end= "")
        print(f"\r CPU usage: |{mem_bar}| {mem_usage:.2f}%", end="\r")

    def display_cpu_and_ram(self):

        while True:
            self.display_usage(psutil.cpu_percent(), psutil.virtual_memory().percent, 30)
            time.sleep(1)

