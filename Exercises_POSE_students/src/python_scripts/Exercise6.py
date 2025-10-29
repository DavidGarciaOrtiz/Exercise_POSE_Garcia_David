from math import pi, radians
from numpy import array, around
from spatialmath.base import * 
import time
from robodk.robolink import *
from robodk.robomath import *
import os

# Define the relative and absolute path to the RoboDK project file
relative_path = "Documentation/Exemples/roboDK/Exemple_UR5e_PickPlace.rdk"
absolute_path = os.path.abspath(relative_path)

# Launch RoboDK and load the project
print('Opening roboDK')
RDK = Robolink()
time.sleep(3) # Wait for RoboDK to be ready and avoid Pop-up for license limitation appears
print('Opening project')
RDK.AddFile(absolute_path)
time.sleep(1) # Not needed but proper solution

# Get the Items and setup
robot = RDK.Item('UR5e')
gripper = RDK.Item("2FG7")
table = RDK.Item("Table")
init = RDK.Item('Init')
targetA = RDK.Item('Target A')
myBrick=RDK.Item("myBrick")
myBrick.setVisible(False)
myBrick.setParent(table)# Do not maintain the actual absolute POSE
poseBrick=xyzrpw_2_pose([-350,-350,30,0,0,0])
myBrick.setPose(poseBrick)

#Define Target B
RDK.AddTarget("Target B")
targetB=RDK.Item("Target B")

R_full = angvec2tr(180,[0.866, 0.000, 0.5], unit='deg')
R = R_full[:3, :3]

eul = tr2eul(R, unit="deg")
rpy = tr2rpy(R, unit="deg", order="zyx") # Math order zyx --> angles order roll/pitch/yaw
ypr = tr2rpy(R, unit="deg", order="xyz") # Math order xyz --> angles order yaw/pitch/roll
a = R[:,2]
o = R[:,1]
angvec = tr2angvec(R, unit="deg")
q=r2q(R)

# Print Orientations
print('R: \n'+ str(around(R,decimals=3)))
print('Euler angles: '+ str(around(eul)))
print('rpy: '+ str(around(rpy)))
print('ypr: '+ str(around(ypr)))
print('Approach: '+ str(around(a,3)) + ' Ortogonal: ' + str(around(o,3)))
print('Angle Vector: ' + str(round(angvec[0])) + "(" + str(around(angvec[1],2)) + ")")
print('Quaternion: '+ str(around(q, 2)))

# Perform Pick & Place
robot.MoveJ(init)
myBrick.setVisible(True)
time.sleep(1)
robot.MoveL(targetA)
myBrick.setParentStatic(gripper)#Maintain the actual absolute POSE
robot.MoveL(targetB)
time.sleep(1)
targetB.Delete()
