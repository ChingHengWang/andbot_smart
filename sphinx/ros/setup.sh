#!/bin/bash

sudo apt-get install ros-indigo-pocketsphinx
#glib.GError: no element "gconfaudiosrc" 
sudo apt-get install gstreamer0.10-gconf

#source code
git clone https://github.com/mikeferguson/pocketsphinx
