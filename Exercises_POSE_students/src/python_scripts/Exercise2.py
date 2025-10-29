import os
import time
import tkinter as tk
from tkinter import messagebox
from robodk.robolink import *    # RoboDK API
from robodk.robomath import *    # Robot math toolbox
from math import radians
from numpy import around

# Define the relative and absolute path to the RoboDK project file
relative_path = "src/roboDK/Exercises1_2.rdk"
absolute_path = os.path.abspath(relative_path)

# Launch RoboDK and load the project
RDK = Robolink(args=absolute_path)

# Retrieve items from the RoboDK station
world = RDK.Item("World")
frame_a = RDK.Item("A-Frame")
frame_b = RDK.Item("B-Frame")
brick = RDK.Item("myBrick")

# Hide the brick initially
brick.setVisible(False)

# Define the initial pose for both frames
initial_pose = TxyzRxyz_2_Pose([30, 40, 50, 0, 0, 0])
frame_a.setParent(world)
frame_b.setParent(world)
frame_a.setPose(initial_pose)
frame_b.setPose(initial_pose)

# Attach the brick to frame B
brick.setParent(frame_b)
brick.setVisible(True)
time.sleep(2)

# Transformation around Fixed frame --> Inverse order --> first Rot, then Trans
def movement_fixed_frame (rotation_x_deg: float, translation_y: float):
    """
    Apply a translation and rotation to frame B and calculate CG positions.
    :param translation_y: Translation along Y-axis in mm
    :param rotation_x_deg: Rotation around X-axis in degrees
    """
    rotation_x_rad = radians(rotation_x_deg)
    final_pose_b = initial_pose * rotx(rotation_x_rad) * transl(0, translation_y, 0)
    frame_b.setPose(final_pose_b)
    time.sleep(2)

    print('Pose of B relative to World: ' + repr(final_pose_b))

    cg_local = [20, 7.5, 10, 1]
    cg_world = final_pose_b * cg_local
    print('CG position relative to World: ' + repr(around(cg_world, decimals=1)))

    cg_relative = rotx(rotation_x_rad) * transl(0, translation_y, 0) * cg_local
    print('CG position relative to A-Frame before movement: ' + repr(cg_local))
    print('CG position relative to A-Frame after movement: ' + repr(around(cg_relative, decimals=1)))

def main():
    """
    Main execution function.
    """
    movement_fixed_frame(rotation_x_deg=45, translation_y=60)

if __name__ == "__main__":
    main()
