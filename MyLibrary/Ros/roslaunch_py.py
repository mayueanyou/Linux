import sys,rospy,roslaunch

def main(name,path):
    rospy.init_node(str(name))
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)
    launch = roslaunch.parent.ROSLaunchParent(uuid, [str(path)])
    launch.start()
    rospy.spin()

def ros_launch(name,path):
    main(name,path)

if __name__=="__main__":
    main(sys.argv[1],sys.argv[2])
