import os,sys
file_path=os.path.abspath(__file__)
current_path =  os.path.abspath(os.path.dirname(file_path) + os.path.sep + ".")
upper_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
sys.path.append(upper_path)
sys.path.append(upper_path+"/trajectory")
sys.path.append(upper_path+"/ddpg_module")
sys.path.append(upper_path+'/simulation')
