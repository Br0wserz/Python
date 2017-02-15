#!/usr/bin/python

import subprocess


trash = open('/dev/null','w')
cmd=['ls','pippo','-l']

a = subprocess.call(cmd, stderr=trash, stdout=trash)
print a
