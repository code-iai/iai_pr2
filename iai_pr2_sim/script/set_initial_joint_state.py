#!/usr/bin/env python

import rospy
from actionlib import ActionClient
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

rospy.init_node('initial_joint_state_setter',
                anonymous=True)
ns = rospy.get_namespace()
ac = ActionClient(u'{}whole_body_controller/body/follow_joint_trajectory'.format(ns), FollowJointTrajectoryAction)
ac.wait_for_server()
goal = FollowJointTrajectoryGoal()
traj = JointTrajectory()
traj.header.stamp = rospy.get_rostime()
traj.joint_names = ['torso_lift_joint',
                    'r_upper_arm_roll_joint',
                    'r_shoulder_pan_joint',
                    'r_shoulder_lift_joint',
                    'r_forearm_roll_joint',
                    'r_elbow_flex_joint',
                    'r_wrist_flex_joint',
                    'r_wrist_roll_joint',
                    'l_upper_arm_roll_joint',
                    'l_shoulder_pan_joint',
                    'l_shoulder_lift_joint',
                    'l_forearm_roll_joint',
                    'l_elbow_flex_joint',
                    'l_wrist_flex_joint',
                    'l_wrist_roll_joint',
                    'head_pan_joint',
                    'head_tilt_joint']

p = JointTrajectoryPoint()
p.positions = [0.1687062500000004,
               0,
               0,
               0,
               0,
               -1.1400000000000001,
               -1.0499999999999998,
               0,
               0,
               0,
               0,
               0,
               -1.1399999999999995,
               -1.0499999999999998,
               0,
               0,
               0]
p.velocities = [0] * len(p.positions)
p.time_from_start = rospy.Duration(1)
traj.points.append(p)
goal.trajectory = traj
ac.send_goal(goal)
