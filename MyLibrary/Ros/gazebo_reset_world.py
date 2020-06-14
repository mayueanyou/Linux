import rospy
from std_srvs.srv import Empty

def main(timeout=None):
    try:
        rospy.wait_for_service('gazebo/reset_world',int(timeout))
        reset_world_prox= rospy.ServiceProxy('gazebo/reset_world', Empty)
        reset_world = reset_world_prox()
    except rospy.ServiceException as e:
        print ("Service call failed: %s"%e)

def gzb_reset_world(timeout=None):
    main(timeout)

if __name__=="__main__":
    main(sys.argv[1])
