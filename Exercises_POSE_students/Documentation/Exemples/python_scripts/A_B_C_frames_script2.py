from robodk.robolink import *
from robodk.robomath import *
from numpy import round, around, array
import os

# Define the relative and absolute path to the RoboDK project file
relative_path = "Documentation/Exemples/roboDK/A_B_C_frames.rdk"
absolute_path = os.path.abspath(relative_path)

# Launch RoboDK and load the project
RDK = Robolink(args=absolute_path)

# Automatically delete previously generated items (Auto tag)
list_items = RDK.ItemList() # list all names
for item in list_items:
    if item.Name().startswith('Auto'):
        item.Delete()
# get the Frame C
frame1 = RDK.Item('A')
frame1_pose=frame1.Pose()
# Add a  frame
RDK.AddFrame("Auto Frame 2")
frame2=RDK.Item("Auto Frame 2")
# Different ways to specify the POSE
frame2_pose=TxyzRxyz_2_Pose([-100,0,0,0,0,pi/2])#Stäubli: RotX*RotY*RotZ 
#frame2_pose=frame1_pose * transl(-100,0,0) * rotz(pi/2)
frame2.setPose(frame2_pose)
myframe_pose=frame2.Pose()
print('Pose Myframe: '+str(myframe_pose))
print('Position Myframe: '+str(around(myframe_pose.Pos(),2)))
print('Orientation Myframe: \n'+str(around(array(myframe_pose.Rot33()).T,2)))
