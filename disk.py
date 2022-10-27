import psutil


class Disk():

    def __init__(self):
        pass


    ## View all of drive
    def view_All_Of_DiskPartitions(self):
        new_list = psutil.disk_partitions()
        for i in new_list:
            lst = list(i)
            print("Disk: " + lst[0][0:1] + " fstype: " + lst[2] + " opts: " + lst[3])


    def view_Space_of_Disk(self):
        Drive = psutil.disk_usage("/")
        print("Total space: " + str(round(Drive.total / 2 ** 30)) + "GB")
        print("Total space: " + str(round(Drive.used / 2 ** 30)) + "GB")
        print("Total space: " + str(round(Drive.free / 2 ** 30)) + "GB")

