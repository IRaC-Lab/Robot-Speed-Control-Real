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


**1. UR3 and Gripper Bring-up**    

    roslaunch ur_gripper_description bringup_with_gripper_85.launch robot_ip:=<YOUR_ROBOT_IP>
    roslaunch robotiq_control cmodel_simple_controller.launch ip:=<YOUR_ROBOT_IP>
    rosrun robotiq_control Gripper_Control.py
    roslaunch ur_gripper_85_moveit_config start_moveit.launch

**2. RealSense Camera Bring-up**   

    roslaunch realsense2_camera rs_camera.launch serial_no:=<YOUR_CAMERA1_SERIAL> camera:=camera1
    roslaunch realsense2_camera rs_camera.launch serial_no:=<YOUR_CAMERA2_SERIAL> camera:=camera2

**3. YOLO-Based Human Distance Measurement via Depth-Color Alignment**  
    
    rosrun realsense2_camera align_depth_to_color.py
    rosrun realsense2_camera depth_distance_seg.py
    rosrun ur_control real_ur_control.py





## License

Each package within this repository is distributed under its respective license. Please refer to each package's original repository for specific licensing information.
