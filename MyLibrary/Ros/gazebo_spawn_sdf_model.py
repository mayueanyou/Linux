import sys,rospy
from gazebo_msgs.srv import SpawnModel
from geometry_msgs.msg import Pose

def main(path,name,x,y,z,timeout=None):
    initial_pose = Pose()
    initial_pose.position.x = float(x)
    initial_pose.position.y = float(y)
    initial_pose.position.z = float(z)

    f = open(path,'r')
    sdf_file = f.read()

    try:
        if(timeout==None):
            rospy.wait_for_service('gazebo/spawn_sdf_model')
        else:
            rospy.wait_for_service('gazebo/spawn_sdf_model',int(timeout))
        spawn_model_prox = rospy.ServiceProxy('gazebo/spawn_sdf_model', SpawnModel)
        spawn_model=spawn_model_prox(name, sdf_file, " ", initial_pose, "world")
        if(spawn_model.success):
            print("gazebo/spawn_sdf_model %s successful!"%str(name))
        else:
            print("gazebo/spawn_sdf_model %s failed!"%str(name))
        return spawn_model.success
    except rospy.ServiceException as e:
        print ("Service call failed: %s"%e)

def gzb_spawn_sdf_model(path,name,x,y,z,timeout=None):
    return main(path,name,x,y,z,timeout)

if __name__=="__main__":
    main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
