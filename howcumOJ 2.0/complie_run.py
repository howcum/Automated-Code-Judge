__author__ = 'howcum'

import os
import subprocess

command = ["g++.exe", "test.cpp" , "-o", "test.exe"]
print (command)

process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

os.system('"C:\\Users\\howcum\\PycharmProjects\\howcumOJ 2.0\\test.exe"')

# command = ["test.exe"]
# process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
