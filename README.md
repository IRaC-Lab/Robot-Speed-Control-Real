# Edge AI-Driven Multi-Camera System for Adaptive Robot Speed Control in Safety-Critical Environments
 Real-World Implementation for "Edge AI-Driven Multi-Camera System for Adaptive Robot Speed Control in Safety-Critical Environments"


## Packages

### 1. Robot-Speed-Control
- **Description**: ROS packages for simulation-based adaptive speed control of the Universal Robots UR3 robotic arm.
- **Source**: [Robot-Speed-Control](https://github.com/IRaC-Lab/Robot-Speed-Control)

### 2. Robotiq-Gripper
- **Description**: ROS packages for Robotiq gripper control and integration.
- **Source**: [robotiq](https://github.com/crigroup/robotiq)



## System Bring-Up Procedure


**1. UR3 + Gripper Bring-up**    

    roslaunch ur_gripper_description bringup_with_gripper_85.launch robot_ip:=<YOUR_ROBOT_IP>
    roslaunch robotiq_control cmodel_simple_controller.launch ip:=<YOUR_ROBOT_IP>
    rosrun robotiq_control Gripper_Control.py
    roslaunch ur_gripper_85_moveit_config start_moveit.launch
    roslaunch realsense2_camera rs_camera.launch serial_no:=<YOUR_CAMERA_SERIAL> camera:=camera1
    roslaunch realsense2_camera rs_camera.launch serial_no:=<YOUR_CAMERA SERIAL> camera:=camera2
    rosrun realsense2_camera align_depth_to_color_sim_mt.py
    rosrun realsense2_camera depth_distance_seg.py
    rosrun ur_control real_ur_control.py





## License

Each package within this repository is distributed under its respective license. Please refer to each package's original repository for specific licensing information.
