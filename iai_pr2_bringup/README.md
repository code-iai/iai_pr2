
How to start the PR2
====================



### Info

To change into 16.04:

    ease@pr2x:~$ chxenial

To change into 20.04:

    ease@pr2x:~$ noetic

To source the ROS workspace:

    ease@pr2x:~$ ros

or

    (ubuntu1604)ease@pr2x:~$ ros


---------------------------------------------------------------------

### Commands

#### roscore

    ease@pr2a:~$ roscore

#### robot drivers

    ease@pr2a:~$ roslaunch /etc/ros/robot.launch

#### occupancy grid, kitchen urdf, kitchen joint state and tf publisher

    (ubuntu1604)ease@pr2a:~$ roslaunch iai_maps no_json_obj.launch

#### localization (map to odom transform), joystick

    ease@pr2a:~$ roslaunch iai_pr2_bringup pr2_manipulation.launch

#### camera driver PR2B

    ease@pr2b:~$ roslaunch /etc/ros/openni_head.launch

#### keeping camera driver alive PR2B

    ease@pr2b:~$ rostopic hz /kinect_head/depth_registered/points

#### robosherlock and knowrob PR2B

    (ubuntu1604)ease@pr2b:~$ roslaunch robosherlock robotvqa.launch # deep learning part
    (ubuntu1604)ease@pr2b:~$ roslaunch robosherlock json_prolog.launch initial_package:=robosherlock # knowrob
    (ubuntu1604)ease@pr2b:~$ roslaunch robosherlock robosherlock.launch # robosherlock itself

#### whole body controller

    ease@pr2a:~$ roslaunch iai_pr2_controller_configuration spawn_whole_body_controller.launch

#### giskard

    (ubuntu1604)ease@pr2b:~$ roslaunch ~/workspace/ros_general/src/iai_pr2/iai_pr2_bringup/launch/giskardpy_with_kitchen.launch # cause iai_pr2 is only in the 14.04 workspace

#### fast IK solver for robot's arms (used by CRAM reasoning)

    ease@pr2a:~$ roslaunch pr2_arm_kinematics pr2_ik_larm_node.launch
    ease@pr2a:~$ roslaunch pr2_arm_kinematics pr2_ik_rarm_node.launch

#### CRAM

This needs to be started outside of byobu, but on the PR2 (in TurboVNC) on PR2B as it uses OpenGL

    (ubuntu1604)ease@pr2b:~$ vglrun roslisp_repl


In the REPL:

    CL-USER> (ros-load:load-system "cram_pr2_pick_place_demo" :cram-pr2-pick-place-demo)
    CL-USER> (roslisp-msg-protocol:md5sum 'giskard_msgs-msg:<movegoal>)
    CL-USER> (roslisp-msg-protocol:ros-datatype 'giskard_msgs-msg:<movegoal>)
    CL-USER> (roslisp-msg-protocol:string-to-ros-msgtype-symbol "giskard_msgs/MoveGoal")
    CL-USER> (roslisp-utilities:startup-ros)
    CL-USER> (demo::demo)

To stop the demo, press Ctrl-C Ctrl-C


### How to pair an unpaired PS3 controller

Connect the PS3 controller (that has "PR2" label on it) to a usb port of pr2a PC (the one on the left, there's a USB port on the back at the top, you can access it if you try).

    sudouser@pr2a:~$ sudo sixpair

You need an account with sudo rights. The ease account doesn't have sudo. Ask somebody with sudo to ssh to the robot and run it for you, if needed.

If you get the error that there is no controller on the USB bus, try ``$ lsusb`` and ensure that it's detected. Unplug and plug again if you have problems.

If no combinations of plugging in / out /sixpair / turning off-on controller help, ``$ sudo poweroff`` is your friend.









---------------------------------------------------------------------

### Useful tools

Check voltage of the 4 battery packs:

    $ rostopic echo /diagnostics |grep -i "voltage=" -A 1

To get the voltage and charge info from the individual batteries:

    $ rostopic echo /diagnostics |grep -i "smart battery" -A 90

Check which users are active on the robot:

    $ robot users

Kill all processes of another user who didn't bother kill his own processes so impolitely:

    $ sudo pkill -u username

Tuck PR2 arms, not sure if this still works:

    $ rosrun pr2_tuckarm tuckarm.py

Debug PR2:

    $ rosrun rqt_pr2_dashboard rqt_pr2_dashboard

