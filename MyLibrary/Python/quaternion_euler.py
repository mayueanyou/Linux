import os,sys,math
import numpy as np

def quaternion_to_euler(x,y,z,w):
    roll = math.atan2(2. * y * z + 2. * w * x,z * z - y * y - x * x + w * w)
    pitch = -math.asin(2. * x * z - 2. * w * y)
    yaw = math.atan2(2. * x * y + 2. * w * z,x * x + w * w - z * z - y * y)
    return {"roll":roll,"pitch":pitch,'yaw':yaw}

def euler_to_quaternion(roll, pitch, yaw):
    qx = np.sin(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) - np.cos(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
    qy = np.cos(roll/2) * np.sin(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.cos(pitch/2) * np.sin(yaw/2)
    qz = np.cos(roll/2) * np.cos(pitch/2) * np.sin(yaw/2) - np.sin(roll/2) * np.sin(pitch/2) * np.cos(yaw/2)
    qw = np.cos(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
    return {"x":qx,"y":qy,'z':qz,'w':qw}

if __name__ == '__main__':
    #print(quaternion_to_rpy(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4])))
    print(euler_to_quaternion(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3])))
