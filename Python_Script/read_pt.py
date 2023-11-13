import os,sys
import torch

if __name__ == '__main__':
    array=torch.load(sys.argv[1])
    print(array)
