import sys
import os

def main(name):
    os.system("rosnode kill "+ str(name))

def ros_node_kill(name):
    main(name)

if __name__=="__main__":
    main(sys.argv[1])
