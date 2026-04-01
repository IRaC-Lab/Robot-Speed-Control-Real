#!/usr/bin/env python3
import os
import sys
import rospy
from robotiq_control.cmodel_base import RobotiqCModel, ComModbusRtu
from robotiq_msgs.msg import CModelCommand, CModelStatus

def mainLoop(device):
    gripper = RobotiqCModel()
    gripper.client = ComModbusRtu()
    rospy.loginfo("Connecting to device " + str(device))
    gripper.client.connectToDevice(device)

    gsta_start_time = None

    def status_callback(status_msg):
        nonlocal gsta_start_time
        if status_msg.gSTA == 3 and gsta_start_time is not None:
            gsta_end_time = rospy.Time.now().to_sec()
            duration = gsta_end_time - gsta_start_time
            rospy.loginfo(f'Gripper "Move" duration: {duration} seconds')
            gsta_start_time = None

    def command_callback(command_msg):
        nonlocal gsta_start_time
        if command_msg.rPR == 0 and gsta_start_time is None:
            gsta_start_time = rospy.Time.now().to_sec()

    rospy.init_node('cmodel_rtu_driver')
    pub = rospy.Publisher('status', CModelStatus, queue_size=3)
    rospy.Subscriber('status', CModelStatus, status_callback)
    rospy.Subscriber('command', CModelCommand, command_callback)

    while not rospy.is_shutdown():
        status = gripper.getStatus()
        pub.publish(status)
        rospy.sleep(0.03)
        gripper.sendCommand()
        rospy.sleep(0.03)

if __name__ == '__main__':
    try:
        mainLoop(sys.argv[1])
    except rospy.ROSInterruptException:
        pass

