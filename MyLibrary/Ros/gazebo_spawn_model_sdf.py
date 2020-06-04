import rospy
import sys
from gazebo_msgs.srv import SpawnModel
from geometry_msgs.msg import Pose

def main(path,name,x,y,z):
    initial_pose = Pose()
    initial_pose.position.x = float(x)
    initial_pose.position.y = float(y)
    initial_pose.position.z = float(z)

    f = open(path,'r')
    sdf_file = f.read()

    rospy.wait_for_service('gazebo/spawn_sdf_model')
    try:
        spawn_model_prox = rospy.ServiceProxy('gazebo/spawn_sdf_model', SpawnModel)
        spawn_model=spawn_model_prox(name, sdf_file, " ", initial_pose, "world")
        return spawn_model.success
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def gzb_spawn_model(path,name,x,y,z):
    return main(path,name,x,y,z)

if __name__=="__main__":
    main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
