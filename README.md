Capture Faces Version 1.3 Written by Tab Aug 2017

This is project is a learning project as our summer project in 2017.

Code source: https://github.com/tabtu/eyesinput
Project managing: https://redmine.cs.uwindsor.ca/projects/eyestracking

Our target is using web camera to locate faces and eyes and analyze eyes’ movements to define some different operation. For example, we can use eyes to control the light switch by opening or closing eyes. Furthermore, we can locate and calculate eyeballs’ movements to control mouse by searching and following the focus.

In this project, here we have finished finding faces and locating eyes on one face, and the program can also detect the changes for the eyes. That means we can get some variable when we are moving eyeballs, such as closing eyes or staring at different places. 

Firstly, we are looking for faces in the video which web camera has got by using OpenCV3.2. The most important step is setting up the programming environment since Python3.6 is only support OpenCV3.2 and we can only install the library by compiling the source code on own computers.
Secondly, to locate the position which eyes are on moving faces is another challenge. We use machine learning and correct image with some algorithm. That makes the program dismiss a lot of error detections. 
Finally, we print these variable on screen every half second. The variable is define from 1 to 100 and we found it will bigger than 10 when we are closing or opening eyes. After finish these part, we use this changing variable to control a light status(open or close).

This project is only a example to show the basic function that moving eyeballs can be tracked by web camera. In addition, we can also use some customized device to track more detail on moving eyeballs since web camera enough distinguishability and images from web camera have a lot of uncontrollable elements in using, such as different illumination and continued moving faces. 

Our suggestion is setting up a mini camera on classes which are focusing on eyeballs will be extremely helpful for further programming. 