cmake_minimum_required(VERSION 3.0.2)
project(iai_pr2_sim)

find_package(catkin REQUIRED COMPONENTS
  iai_pr2_description
#   iai_naive_kinematics_sim
  robot_state_publisher
#   omni_pose_follower
  tf2_ros)

catkin_package()

include_directories(
# include
# ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS 
	script/set_initial_joint_state.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})