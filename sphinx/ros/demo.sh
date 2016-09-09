#!/bin/bash

# run recognizer
#choose 1 
rosrun pocketsphinx recognizer.py _lm:=`rospack find pocketsphinx`/demo/robocup.lm _dict:=`rospack find pocketsphinx`/demo/robocup.dic

#choose 2 : move 
rosrun pocketsphinx recognizer.py _lm:=`rospack find pocketsphinx`/demo/voice_cmd.lm _dict:=`rospack find pocketsphinx`/demo/voice_cmd.dic

# call service to start
rosservice call /recognizer/start "{}"
