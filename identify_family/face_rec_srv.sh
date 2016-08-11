#!/bin/bash

roscore &
sleep 3
rosrun identify_family face_rec_client_android &
rosrun identify_family face_rec_srv 

