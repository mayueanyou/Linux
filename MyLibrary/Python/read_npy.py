import os,sys
import numpy as np

if __name__ == '__main__':
    array=np.load(sys.argv[1],allow_pickle=True)
    print(array)
