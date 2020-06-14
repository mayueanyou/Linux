import rospy
import sys
from gazebo_msgs.srv import DeleteModel

def main(name,timeout=None):
    try:
        rospy.wait_for_service('gazebo/delete_model',int(timeout))
        delete_model_prox = rospy.ServiceProxy('gazebo/delete_model',DeleteModel)
        delete_model = delete_model_prox(name)
        return delete_model.success
    except rospy.ServiceException as e:
        print ("Service call failed: %s"%e)
        return False

def gzb_delete_model(name,timeout=None):
    return main(name,timeout)

if __name__=="__main__":
    main(sys.argv[1],sys.argv[2])
