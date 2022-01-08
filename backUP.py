import shutil
import os

src = input("Enter the folder for which u want to create the backups: ")
destination = input("Enter the destination folder")
src = src+'/'
destination = destination+'/'
files = os.listdir(src)
for file in files:
    shutil.copy(src+file,destination)
