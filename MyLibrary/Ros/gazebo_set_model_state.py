import sys,rospy
from gazebo_msgs.srv import SetModelState
from gazebo_msgs.msg import ModelState
from Ros import gazebo_get_model_state
from geometry_msgs.msg import*

def main(name,poi_x='*',poi_y='*',poi_z='*',ori_x='*',ori_y='*',ori_z='*',ori_w='*',
    lin_x='*',lin_y='*',lin_z='*',ang_x='*',ang_y='*',ang_z='*',timeout=None):
    modelstate=ModelState()
    pose = Pose()
    twist= Twist()
    pose,twist=gazebo_get_model_state.main(str(name),"world",timeout)
    if(poi_x!='*'):
        pose.position.x = float(poi_x)
    if(poi_y!='*'):
        pose.position.y = float(poi_y)
    if(poi_z!='*'):
        pose.position.z = float(poi_z)
    if(ori_x!='*'):
        pose.orientation.x=float(ori_x)
    if(ori_y!='*'):
        pose.orientation.y=float(ori_y)
    if(ori_z!='*'):
        pose.orientation.z=float(ori_z)
    if(ori_w!='*'):
        pose.orientation.w=float(ori_w)
    if(lin_x!='*'):
        twist.linear.x=float(lin_x)
    if(lin_y!='*'):
        twist.linear.y=float(lin_y)
    if(lin_z!='*'):
        twist.linear.z=float(lin_z)
    if(ang_x!='*'):
        twist.angular.x=float(ang_x)
    if(ang_y!='*'):
        twist.angular.y=float(ang_y)
    if(ang_z!='*'):
        twist.angular.z=float(ang_z)
    modelstate.model_name=name
    modelstate.pose=pose
    modelstate.twist=twist
    modelstate.reference_frame="world"

    try:
        if(timeout==None):
            rospy.wait_for_service('gazebo/set_model_state')
        else:
            rospy.wait_for_service('gazebo/set_model_state',int(timeout))
        set_model_state_prox = rospy.ServiceProxy('gazebo/set_model_state', SetModelState)
        set_model_state_prox(modelstate)
        print("gazebo/set_model_state %s!"%str(name))
    except rospy.ServiceException as e:
        print ("Service call failed: %s"%e)

def gzb_set_model_state(name,poi_x='*',poi_y='*',poi_z='*',ori_x='*',ori_y='*',ori_z='*',ori_w='*',
    lin_x='*',lin_y='*',lin_z='*',ang_x='*',ang_y='*',ang_z='*',timeout=None):
    main(name,poi_x,poi_y,poi_z,ori_x,ori_y,ori_z,ori_w,lin_x,lin_y,lin_z,ang_x,ang_y,ang_z,timeout)

if __name__=="__main__":
    main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8],
    sys.argv[9],sys.argv[10],sys.argv[11],sys.argv[12],sys.argv[13],sys.argv[14],sys.argv[15])
