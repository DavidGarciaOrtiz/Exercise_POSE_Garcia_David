# Type help("robodk.robolink") or help("robodk.robomath") for more information
# Press F5 to run the script
# Documentation: https://robodk.com/doc/en/RoboDK-API.html
# Reference:     https://robodk.com/doc/en/PythonAPI/robodk.html
# Note: It is not required to keep a copy of this file, your Python script is saved with your RDK project

# You can also use the new version of the API:
from robodk.robolink import *    # RoboDK API
from robodk.robomath import *    # Robot toolbox
from math import pi
import time

RDK = Robolink()

World=RDK.Item("World")
Aframe=RDK.Item("A-Frame")
Bframe=RDK.Item("B-Frame")
myBrick=RDK.Item("myBrick")
myBrick.setVisible(False)
myBrick.setParent(World)#Do not maintain the actual absolute POSE

Aframe_init = TxyzRxyz_2_Pose([0, 0, 0, 0, 0, 0])
Bframe_init = Aframe_init
Aframe.setPose(Aframe_init)
Bframe.setPose(Bframe_init)
time.sleep(2)

# Set myBrick nested to B-Frame
myBrick.setParentStatic(Bframe)#Maintains the actual absolute POSE
myBrick.setVisible(True)
time.sleep(2)

#Move the object with transformation
Bframe_final1=Bframe_init*transl(50,0,0)
Bframe.setPose(Bframe_final1)
time.sleep(2)

#Move the object with transformation
Bframe_final2=Bframe_final1*rotz(pi/4)
Bframe.setPose(Bframe_final2)
time.sleep(2)