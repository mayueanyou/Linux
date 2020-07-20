import sys,rospy,roslaunch

def main(name,package,executable,spin,arg="None"):
    rospy.init_node(str(name))
    if(arg=="None"):
        node = roslaunch.core.Node(str(package), str(executable))
    else:
        node = roslaunch.core.Node(str(package), str(executable),args=arg)

    launch = roslaunch.scriptapi.ROSLaunch()
    launch.start()
    process = launch.launch(node)
    if(spin=="True"):
        rospy.spin()

def ros_run(name,package,executable,spin,arg="None"):
    main(name,package,executable,arg)

if __name__=="__main__":
    main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
