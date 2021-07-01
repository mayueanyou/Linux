import os,sys
import numpy as np

np.set_printoptions(threshold=np.inf)

if __name__ == '__main__':
    array=np.load(sys.argv[1],allow_pickle=True)
    print(array)
    print("size")
    print(array.shape)
