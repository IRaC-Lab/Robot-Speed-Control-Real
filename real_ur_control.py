#!/usr/bin/env python3
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import math
import argparse
import random
import time
import csv
from datetime import datetime
import numpy as np
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import Pose, PoseStamped
from geometry_msgs.msg import Point
from std_msgs.msg import Float32
from std_msgs.msg import String
from shape_msgs.msg import SolidPrimitive
from gazebo_msgs.srv import GetModelProperties, GetModelState
from gazebo_msgs.msg import ModelState
from moveit_commander import PlanningSceneInterface
from moveit_commander import PlanningScene
from visualization_msgs.msg import Marker
from queue import Queue

np.set_printoptions(suppress=True)
np.set_printoptions(linewidth=np.inf)

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node("ur_control", anonymous=True)
group_name_m = "arm"
move_group_m = moveit_commander.MoveGroupCommander(group_name_m)
display_trajectory_publisher = rospy.Publisher("/move_group/display_planned_path", moveit_msgs.msg.DisplayTrajectory, queue_size=10)
scene = moveit_commander.PlanningSceneInterface()
move_group_m.set_max_velocity_scaling_factor(1.0)

def add_static_obstacle():
    object1_name = "ur_base_modify"
    object1_pose = geometry_msgs.msg.PoseStamped()
    object1_pose.header.frame_id = "world"
    object1_pose.pose.orientation.w = 1.0
    object1_pose.pose.position.x = 0 
    object1_pose.pose.position.y = 0 
    object1_pose.pose.position.z = -0.02
    
    object2_name = "test_box"
    object2_pose = geometry_msgs.msg.PoseStamped()
    object2_pose.header.frame_id = "world"
    object2_pose.pose.orientation.w = 1.0
    object2_pose.pose.position.x = 0
    object2_pose.pose.position.y = 0.5
    object2_pose.pose.position.z = -0.44
    
    scene.add_box(object1_name, object1_pose, size=(0.5, 0.5, 0.02))
    scene.add_box(object2_name, object2_pose, size=(0.5, 0.45, 0.72))

def subscriber():
    global result
    point_sub = rospy.Subscriber('scaling_factor', Float32, callback, queue_size = 3)
    rospy.on_shutdown(shutdown_hock)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pnp_loop()
        rate.sleep()

def callback(data):
    global num
    print(data.data)
    scaling_factor = data.data
    scaling_factor = float(scaling_factor)
    move_group_m.set_max_velocity_scaling_factor(scaling_factor)
    move_group_m.stop()

def shutdown_hock():
    rospy.loginfo("Shutting down the node")
    rospy.signal_shutdown("Ctrl + C received")

def waypoint_1():
    global joint_goal_m
    joint_goal_m = move_group_m.get_current_joint_values()
    joint_goal_m = [-4.63015, -0.75169, 0.42621, 5.0926, 4.71405, 0.08148]
    move_group_m.go(joint_goal_m, wait=True)

def waypoint_2():
    global joint_goal_m
    joint_goal_m = move_group_m.get_current_joint_values()
    joint_goal_m = [-4.63011, -0.77373, 1.03833, 4.50239, 4.71475, 0.08062]
    move_group_m.go(joint_goal_m, wait=True)

def waypoint_3():
    global joint_goal_m
    joint_goal_m = move_group_m.get_current_joint_values()
    joint_goal_m = [-5.26786, -0.75585, 0.43861, 5.07469, 4.68154, -0.55541]
    move_group_m.go(joint_goal_m, wait=True)

def waypoint_4():
    global joint_goal_m
    joint_goal_m = move_group_m.get_current_joint_values()
    joint_goal_m = [-5.26763, -0.77378, 1.04232, 4.48856, 4.68074, -0.55594]
    move_group_m.go(joint_goal_m, wait=True)

scaling_factor = 1.0
num = 0
pub = rospy.Publisher('gripper_cmd', String, queue_size=3)

def pnp_loop():
    global num
    num += 1
    if num == 1:
        waypoint_1()
        print(f"current_num: {num}")
    elif num == 2:
        waypoint_2()
        print(f"current_num: {num}")
    elif num == 3:
        pub.publish("c")
        print("close")
        rospy.sleep(1)
    elif num == 4:
        waypoint_1()
        print(f"current_num: {num}")

    elif num == 5:
        waypoint_3()
        print(f"current_num: {num}")
    elif num == 6:
        waypoint_4()
        print(f"current_num: {num}")
    elif num == 7:
        pub.publish("o")
        print("open")
        rospy.sleep(1)
    elif num == 8:
        waypoint_3()
        print(f"current_num: {num}")

    elif num == 9:
        waypoint_3()
        print(f"current_num: {num}")
    elif num == 10:
        waypoint_4()
        print(f"current_num: {num}")
    elif num == 11:
        pub.publish("c")    
        print("close")
        rospy.sleep(1)
    elif num == 12:
        waypoint_3()
        print(f"current_num: {num}")

    elif num == 13:
        waypoint_1()
        print(f"current_num: {num}")
    elif num == 14:
        waypoint_2()
        print(f"current_num: {num}")
    elif num == 15:
        pub.publish("o")
        print("open")
        rospy.sleep(1)
    elif num == 16:
        waypoint_1()
        print(f"current_num: {num}")
       
    elif num == 17:
        num = 0

if __name__ == '__main__':
    try:
        pub.publish("a")
        add_static_obstacle()
        subscriber()
        pub.publish("r")
    except rospy.ROSInterruptException:
        pass
