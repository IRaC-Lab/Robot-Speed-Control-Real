#!/usr/bin/env python3
import rospy
from robotiq_msgs.msg import CModelCommand
from std_msgs.msg import String
from time import sleep

def gripper_control(char,pub):
    command = CModelCommand()
    if char == 'o':
        command.rPR = 0
    elif char == 'c':
        command.rPR = 220
    elif char == 'r':
        command.rACT = 0
    else:
        return
    command.rACT = 1
    command.rGTO = 1
    command.rSP = 255
    command.rFR = 150
    pub.publish(command)
    rospy.sleep(1.0)  # Optional: Sleep for some time to allow the gripper to complete the action

def callback(data, pub):
    str_data = str(data.data)
    print("Received command:", str_data)
    gripper_control(str_data, pub)

def subscriber():
    rospy.init_node('Gripper_Control')
    pub = rospy.Publisher('command', CModelCommand, queue_size=3)
    sub = rospy.Subscriber('gripper_cmd', String, callback, pub)

    while not rospy.is_shutdown():
        rospy.spin()

if __name__ == '__main__':
    subscriber()
