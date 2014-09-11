#!/usr/bin/python
import os
from os.path import join, getsize

def get_next_demo(current_name, demos):
    hit = False
    for demo in demos.items():
        if hit:
            return demo
        if current_name == demo[0]:
            hit = True
    return demos.items()[0]

def write_current_demo(name):
    with open(current_file, "w") as file:
        file.write(name)
        file.close()

current_dir  = '/home/dimo/current_demo'
demos_dir    = '/home/dimo/demos/'
current_file = '/tmp/current_demo'

if not os.path.isfile(current_file):
    for dir in os.listdir(renderers):
        print "No renderer currently running... starting with " + dir
        write_current_demo(dir)
        break


with open(current_file, "r") as file:
    current_name = file.read()
    file.close()

demos = {}
for dir in os.listdir(demos_dir):
    about_file = demos_dir + dir + "/about.html"
    if os.path.isfile(about_file):
        demos[dir] = {}
        demos[dir]['name'] = dir
        demos[dir]['path'] = demos_dir + dir + '/run/'
        demos[dir]['about_file'] = about_file
        
print "Current demo is " + current_name

demo = get_next_demo(current_name, demos)[1]
print "New demo is " + demo['name']
write_current_demo(demo['name'])

try :
    os.unlink(current_dir)
except:
    print "foo"
    
os.symlink(demo['path'], current_dir)
