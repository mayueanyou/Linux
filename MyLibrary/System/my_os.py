import sys
import os

def main(name):
    os.system(str(name))

def my_os(name):
    main(name)

def my_os_new(name):
    os.system("gnome-terminal -- " + "%s" %str(name))

if __name__=="__main__":
    main(sys.argv[1])
