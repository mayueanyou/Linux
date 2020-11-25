import os,sys,math

def q_to_rpy(x,y,z,w):
    roll = math.atan2(2. * y * z + 2. * w * x,z * z - y * y - x * x + w * w)
    pitch = -math.asin(2. * x * z - 2. * w * y)
    yaw = math.atan2(2. * x * y + 2. * w * z,x * x + w * w - z * z - y * y)
    rpy={"roll":roll,"pitch":pitch,'yaw':yaw}
    return rpy


if __name__ == '__main__':
    print(quaternion_to_rpy(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4])))
