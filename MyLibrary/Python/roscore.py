import os,sys,rospy

while True:
    try:
        rospy.get_master().getPid()
    except:
        os.system("roscore")
