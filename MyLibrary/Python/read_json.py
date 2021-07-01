import os,sys
import json

if __name__ == '__main__':
    with open(sys.argv[1],'r') as load_f:
        load_dict = json.load(load_f)
        print(load_dict)
