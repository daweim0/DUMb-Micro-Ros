# DUMb-Micro-Ros (dummr)

Dummr is a simpler alternative to Micro-ROS and Rosserial. Dummr is designed for simplicity, quick prototyping, and to frustrate performance freaks.

### Features:
* Dummr is easy to build
    * Dummr is a header only library
    * Dummr does not wrap the build system (like rosserial)
    * Dummr does not require message definitions to be compiled

* Dummr is simple to use
    * Look how simple this example is - [https://github.com/daweim0/DUMb-micro-ros/blob/main/arduino_code/arduino_code.ino](https://github.com/daweim0/DUMb-micro-ros/blob/main/arduino_code/arduino_code.ino)

* Dummr is debuggable
    * Data is sent over serial in JSON (human readable). Grab your logic analyzer and go to town!


### Instructions:

1. Copy [dummr.h](https://github.com/daweim0/DUMb-micro-ros/blob/main/arduino_code/dummr.h) and [ArduinoJsonV6.h](https://github.com/daweim0/DUMb-micro-ros/blob/main/arduino_code/ArduinoJsonv6.h) into wherever you keep header files.
2. Clone this entire repo into your catkin workspace (or copy and paste, git submodules can be a pain to use)
4. Connect and program your favorite arduino-compatible microcontroller. Be sure to call dummr_init() at the start of your program and dummr_check_for_msg() reguarly.
3. Do a catkin build and run `rosrun dumb-micro-ros dumb_micro_ros.py _serial_port:="/dev/ttyS6"` to start the dummr server (or put it in a rosalunch file, I don't care)


### Notes:
* Dummr is not enterprise grade, it's for quick hacking
* Dummr is not for speed freaks (but it's probably fast enough for everyone else)
* only topic pub/sub is supported (no services or actions)

### Licence(s):
There's code in this repo under BSD, MIT, and Creative Commons licences.
