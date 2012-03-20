#!/usr/bin/python
import os

os.system("ls $RACKSCHOOL/usr > $RACKSCHOOL/public/userlist.txt")

userlist = open("./public/userlist.txt", "r")
print userlist.read()
header = open("./public/header.html", "r")
header = header.read()
output = open("./public/index.html", "w")
html = ''

output.write(html)
