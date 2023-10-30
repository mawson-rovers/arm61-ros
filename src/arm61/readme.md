# Installing:

Add this package to your `src` folder in your ROS workspace.

Install dependencies using (may require initialisation [see [rosdep docs](https://docs.ros.org/en/foxy/Tutorials/Intermediate/Rosdep.html)]):

`> rosdep install --from-paths src -y --ignore-src`

# Building:

Build code normally using:

`> colcon build`

Don't forget to source `setup.bash` to update environment variables using:

`> source <ROS workspace>/install/setup.bash`

# Running:

The demo can be launched using the included launch file. The original can be modified in `<ROS workspace>/src/arm61/launch/arm61.launch.py`.

Inside this file you can select the high or low resolution model, by uncommenting the prefered line. By default the high resolution model is used, but this may create performance problems on less powerful systems.

A rebuild is required to make any changes effective. Then running:

`> ros2 launch arm61 arm61.launch.py`

This will start RVIZ and the joint state publisher GUI.

# RVIZ:

An RVIZ configuration is stored in `<ROS workspace>/src/arm61/rviz/arm61.rviz`. This file is automatically opened when launching the demo using the launch file.

Any permanant RVIZ layout changes made should be written to this file. A rebuild is required before restarting RVIZ using the launch file.

# URDF config:

There are two URDF config files; a low and high resolution version. They are identical except use different `.stl` files from their respective folders.

At some point it may be necessary to adjust the joint speed and effort values, be sure to modify both files.