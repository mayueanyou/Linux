import rospy
import sys
from gazebo_msgs.srv import GetModelState
from geometry_msgs.msg import*

def main(model_name,relative_entity_name,timeout=None):
    try:
        rospy.wait_for_service('gazebo/get_model_state',int(timeout))
        get_model_state_prox = rospy.ServiceProxy('gazebo/get_model_state', GetModelState)
        get_model_state=get_model_state_prox(model_name,relative_entity_name)
        return get_model_state.pose,get_model_state.twist
    except rospy.ServiceException as e:
        print ("Service call failed: %s"%e)

def gzb_get_model_state(model_name,relative_entity_name,timeout=None):
    pose=Pose()
    twist=Twist()
    pose,twist=main(model_name,relative_entity_name,timeout)
    return pose,twist

if __name__=="__main__":
    main(sys.argv[1],sys.argv[2],sys.argv[3])
