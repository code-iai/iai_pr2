# iai_pr2

Installation, configuration, and launch files specific to IAI's PR2 robot.

## Explanation of different model versions

* `pr2_calibrated_with_ft2.xml` is the current model of the PR2 with the force torque sensor. The model is similar to `/etc/ros/indigo/urdf/robot.xml` on *pr2a* except for additional mimic joints.
* `pr2_calibrated_with_ft2_cableguide.xml` is the current model of the PR2 with the force torque sensor and the cable guide made of item profiles. This model is derived from `pr2_calibrated_with_ft2.xml`.

The simulation launch files with `_cableguide` in the name also use the new model with the cable guide and are based on the similar named launch files with or without odom joints.

The real robot uses its own model and launch file stored at `/etc/ros/indigo/` on *pr2a*. The launch file `iai_pr2_bringup/launch/robot.launch` is derived from the launch file `/etc/ros/indigo/robot.launch` on *pr2a*. Both include the force torque sensor but not the cable guide.

The launch `iai_pr2_bringup/launch/robot_with_cableguide.launch` is derived from `iai_pr2_bringup/launch/robot.launch` and uses the new model with cable guide.
