from robodk.robolink import *
from robodk.robomath import *
from numpy import round, around, array
import os

# Define the relative and absolute path to the RoboDK project file
relative_path = "Documentation/Exemples/roboDK/A_B_C_frames.rdk"
absolute_path = os.path.abspath(relative_path)

# Launch RoboDK and load the project
RDK = Robolink(args=absolute_path)

# Program example:
frame1 = RDK.Item('C')
if frame1.Valid():
    pose=frame1.Pose() #MAT structure stored in column-major order
    pose_array=array(pose).T #array structure stored in row-major order
    # Obtain the translation xyz and Rotation rotx roty rotz
    TRxyz = Pose_2_TxyzRxyz(pose)#RotX*RotY*RotZ
    position = pose.Pos()
    orientation=array(pose.Rot33()).T
    print('Item selected: ' + frame1.Name())
    print('POSE: ' + str(pose))
    print('POSE array: \n' + str(around(pose_array,2)))
    print('TxyzRxyz: ' + str(around(TRxyz,2)))
    print('Position: ' + str(around(position,2)))
    print('Orientation array: \n' + str(around(orientation,2)))
    
else:
    print('Items in the station:')
    itemlist = RDK.ItemList()
    for item in itemlist:
      print(item.Name())   
