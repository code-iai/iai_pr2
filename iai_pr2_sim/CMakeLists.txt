cmake_minimum_required(VERSION 2.8.3)
project(iai_pr2_sim)

find_package(catkin REQUIRED COMPONENTS
  iai_pr2_description
  iai_naive_kinematics_sim
  robot_state_publisher
  omni_pose_follower
  tf2_ros)

catkin_package()
