from gazebo_get_model_state import*
from geometry_msgs.msg import*
from gazebo_delete_model import*

try:
    bool=gzb_delete_model("cube1",1)
except:
    print("gan")
