# Edge AI-Driven Multi-Camera System for Adaptive Robot Speed Control in Safety-Critical Environments
 Real-World Implementation for "Edge AI-Driven Multi-Camera System for Adaptive Robot Speed Control in Safety-Critical Environments"



https://github.com/user-attachments/assets/6ff931fb-54b5-4962-b027-2ad753715b6f


## Packages

### 1. Robot-Speed-Control
- **Description**: ROS packages for simulation-based adaptive speed control of the Universal Robots UR3 robotic arm.
- **Source**: [Robot-Speed-Control](https://github.com/IRaC-Lab/Robot-Speed-Control)

### 2. Robotiq-Gripper
- **Description**: ROS packages for Robotiq gripper control and integration.
- **Source**: [robotiq](https://github.com/crigroup/robotiq)


## Prerequisites

- This repository assumes that `Robot-Speed-Control` has already been set up in your ROS workspace.
- For additional packages such as `robotiq`, please refer to their original repositories for dependency installation and setup instructions.
- Place each package in the appropriate location according to your local workspace structure.



## System Bring-Up Procedure

### Notes
- Replace `<YOUR_ROBOT_IP>` with the actual IP address of the UR3 robot (e.g., `robot_ip:=172.16.0.2`).
- Replace `<YOUR_CAMERA1_SERIAL>` and `<YOUR_CAMERA2_SERIAL>` with the serial numbers of the RealSense cameras (e.g., `serial_no:=920312072876`).
- Before running `align_depth_to_color.py`, update the depth subscriber in the script to match your RealSense depth topic.
- Before running `rosrun ur_control real_ur_control.py`, place `real_ur_control.py` in `ur3/ur_control/scripts`.
- Make sure the robot, gripper, and cameras are connected before running the commands.
- Run commands in separate terminals when necessary.

**1. UR3 and Gripper Bring-up**   

```bash
roslaunch ur_gripper_description bringup_with_gripper_85.launch robot_ip:=<YOUR_ROBOT_IP>
```
```bash
roslaunch robotiq_control cmodel_simple_controller.launch ip:=<YOUR_ROBOT_IP>
```
```bash
rosrun robotiq_control Gripper_Control.py
```
```bash    
roslaunch ur_gripper_85_moveit_config start_moveit.launch
```

**2. RealSense Camera Bring-up**   

```bash
roslaunch realsense2_camera rs_camera.launch serial_no:=<YOUR_CAMERA1_SERIAL> camera:=camera1
```
```bash    
roslaunch realsense2_camera rs_camera.launch serial_no:=<YOUR_CAMERA2_SERIAL> camera:=camera2
```

**3. YOLO-Based Human Distance Measurement via Depth-Color Alignment**  

```bash
cd catkin_ws/src/Robot-Speed-Control/yolov5/segment
python3 predict.py --conf 0.7
```

```bash    
rosrun realsense2_camera align_depth_to_color.py
```
```bash
rosrun realsense2_camera depth_distance_seg.py
```

**4. Adaptive Speed Control for UR3 Waypoint Motion** 

```bash
rosrun ur_control real_ur_control.py
```




## License

Each package within this repository is distributed under its respective license. Please refer to each package's original repository for specific licensing information.
