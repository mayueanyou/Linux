import rospy
from std_srvs.srv import Empty

def main(timeout=None):
    try:
        rospy.wait_for_service('gazebo/reset_simulation',int(timeout))
        reset_simulation_prox= rospy.ServiceProxy('gazebo/reset_simulation', Empty)
        reset_simulation = reset_simulation_prox()
    except rospy.ServiceException as e:
        print ("Service call failed: %s"%e)

def gzb_reset_simulation(timeout=None):
    main(timeout)

if __name__=="__main__":
    main(sys.argv[1])
