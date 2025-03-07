
How to start the PR2
====================

#### Log into PR2-EXT

Go to the apartment lab on the ground floor.
Log into `ease` user on `pr2-ext` PC (the PCs are labeled).
The password is in the iai wiki, you need to be logged in: https://ai.uni-bremen.de/wiki/intern/pr2

#### Terminator setup on PR2-EXT

Find the terminator with the robot launch file tabs.
If you had to restart PR2-EXT or accidentally killed the Terminator, start the old layout with:

    ease@pr2-ext:~$ terminator -l demo

In every terminal, you need to source the LispCramp workspace

    ease@pr2-ext:~$ source_cram

### Commands to start on PR2A

#### Byobu on PR2A

Log in into `ease` user on `PR2A` PC (it's located in PR2's feet) and start Byobu (it's like TMux):

    ease@pr2-ext:~$ ssh ease@pr2a
    ease@pr2a:~$ byobu

Byobu key bindings:

  * change tab go left: F3
  * change tab go right: F4
  * change horizontally split tab go down: Shift-Down
  * change horizontally split tab go up: Shift-Up
  * new tab: F2
  * close tab: Ctrl-D
  * rename tab: F8
  * detach from Byobu without killing it: F6
  * open Byobu after detaching from it: ease@pr2a:~$ byobu

#### roscore on PR2A

Find the tab in Byobu named `core`. If tabs don't have names, go to the first tab. Start `roscore`:

    ease@pr2a:~$ roscore    

#### robot drivers on PR2A

    ease@pr2a:~$ roslaunch /etc/ros/robot.launch

#### map, localization (map to odom transform), joystick on PR2A

    ease@pr2a:~$ roslaunch iai_pr2_bringup pr2_map_joy_amcl.launch

### Commands to start on PR2B

#### camera driver on PR2B

Make sure you're on PR2B in Byobu. If not, open a new Byobu tab (F2) and ssh to PR2B: `ssh pr2b`.

    ease@pr2b:~$ roslaunch /etc/ros/openni_head.launch

#### keeping camera driver alive on PR2B

    ease@pr2b:~$ rostopic hz /kinect_head/depth_registered/points

### Commands to start on PR2-EXT

Switch the Terminator tab.

#### kitchen urdf, kitchen joint state and tf publisher on PR2-EXT

    ease@pr2-ext:~$ roslaunch cram_projection_demos everything.launch pr2:=true apartment:=true upload_robot:=false tf2_buffer:=true

#### giskard on PR2-EXT

    ease@pr2-ext:~$ roslaunch giskardpy giskardpy_pr2_iai.launch

#### RoboKudo on PR2-EXT

    ease@pr2-ext:~$ rosrun robokudo start_rk_query.sh

#### Localize the robot on PR2-EXT

    ease@pr2-ext:~$ rviz
    
*MAKE SURE PR2 IS WELL LOCALIZED!*
In Rviz, click the `2D Pose Estimate` button, look at the red arrow cloud and the laser scan fitting the apartment outline.
Press the START button on ESTOP.
Drive around with the Joystick until well localized.

#### CRAM

    ease@pr2-ext:~$ emacs &

In emacs:

    Ctrl-c l

    CL-USER> (ros-load:load-system "cram_projection_demos" :cram-projection-demos)
    CL-USER> (ros-load:load-system "cram_pr2_process_modules" :cram-pr2-process-modules)
    CL-USER> (roslisp-utilities:startup-ros)
    CL-USER> (pr2-pms:with-real-robot
         	(demos::apartment-demo-merged :step 0))

To stop the demo, press Ctrl-C Ctrl-C, Step 0 = all, Step 1  = opening/pick and place/closing, Step 2 = pouring

------------------------------------------------------------

#### KnowRob logging on PR2-EXT

    ease@pr2-ext:~$ roslaunch knowrob knowrob.launch

If knowrob complains about rosprolog or mongo, start mongo.
If knowrob doesn't complain, mongo is already started.
So, first check the status and the start the process

    ease@pr2-ext:~$ sudo systemctl status mongod
    ease@pr2-ext:~$ sudo systemctl start mongod

#### To collect NEEMs, do this in CRAM:

    CL-USER> (ros-load:load-system "cram_cloud_logger" :cram-cloud-logger)
    CL-USER> (setf cram-tf:tf-broadcasting-enabled nil)
    CL-USER> (roslisp-utilities:startup-ros)
    CL-USER> (ccl::start-episode)
    CL-USER> (pr2-pms:with-real-robot
               (demos::apartment-demo))
    CL-USER> (ccl::stop-episode)

-----------------------------------------------

## troubleshooting:
### giskard doesn't work
if you see

    [ERROR] [1671016974.953925]: [/giskard]: '/l_arm_controller/follow_joint_trajectory' preempted, probably because it took to long to execute the goal.

then the time between pr2-ext and pr2 is probably off, you can check

    $ rostopic delay /joint_states
    
you can fix this by restarting crony

    service chrony restart



### DEPRECATED STUFF: robosherlock and knowrob PR2B

    (ubuntu1604)ease@pr2b:~$ roslaunch robosherlock robotvqa.launch # deep learning part
    (ubuntu1604)ease@pr2b:~$ roslaunch robosherlock json_prolog.launch initial_package:=robosherlock # knowrob
    (ubuntu1604)ease@pr2b:~$ roslaunch robosherlock robosherlock.launch # robosherlock itself


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

To change into 16.04:

    ease@pr2x:~$ chxenial

To change into 20.04:

    ease@pr2x:~$ noetic
