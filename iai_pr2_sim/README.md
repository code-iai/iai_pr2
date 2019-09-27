# iai_pr2_sim
A lightweight kinematics simulation of IAI's PR2 robot.

# setup workspace
```
source /opt/ros/kinetic/setup.bash
mkdir -p iai_pr2_sim_ws/src
cd iai_pr2_sim_ws
catkin init
cd src
wstool init
wstool merge https://raw.githubusercontent.com/code-iai/iai_pr2/master/iai_pr2_sim/rosinstall/catkin.rosinstall
wstool update
rosdep install --ignore-src --from-paths iai_pr2/iai_pr2_sim/
cd ..
catkin build
source devel/setup.bash
```

# start sim
```
roslaunch iai_pr2_sim ros_control_sim_with_base.launch
```
