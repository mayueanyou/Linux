#!/usr/bin/env python

import rospy
import sys
from gazebo_msgs.srv import DeleteModel

def main(name):
    rospy.wait_for_service('gazebo/delete_model')
    try:
        delete_model_prox = rospy.ServiceProxy('gazebo/delete_model',DeleteModel)
        delete_model = delete_model_prox(name)
        return delete_model.success
    except rospy.ServiceException as e:
        print ("Service call failed: %s"%e)

def gzb_delete_model(name):
    return main(name)

if __name__=="__main__":
    main(sys.argv[1])
