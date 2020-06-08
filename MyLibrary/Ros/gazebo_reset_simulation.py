#!/usr/bin/env python

import rospy
from std_srvs.srv import Empty

def main():
    rospy.wait_for_service('gazebo/reset_simulation')
    try:
        reset_simulation_prox= rospy.ServiceProxy('gazebo/reset_simulation', Empty)
        reset_simulation = reset_simulation_prox()
    except rospy.ServiceException as e:
        print ("Service call failed: %s"%e)

def gzb_reset_simulation():
    main()

if __name__=="__main__":
    main()
