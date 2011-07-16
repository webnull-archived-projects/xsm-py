#!/usr/bin/python
import os, re

Device = "/dev/sdb1"
put,get = os.popen4("mount")
result = get.read()

mountPoint = re.findall(Device+" on (.*) type", result)

if len(mountPoint) == 1:
    print mountPoint[0]
