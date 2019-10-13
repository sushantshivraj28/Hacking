#!/usr/bin/python3

import subprocess

interface = input("Enter your interface name : ")

new_mac = input("Enter the 12 digit hexadecimal mac address :")

subprocess.call(["ifconfig" , interface  "down"])

subprocess.call(["ifconfig" , interface , "hw" , "ether" , new_mac ])

subprocess.call(["ifconfig" , interface , "up"])

subprocess.call(["ifconfig" , interface])
