#include "ros/ros.h"
#include "identify_family/BuildModel.h"
#include <stdio.h>
#include <iostream>

bool build_model(identify_family::BuildModel::Request &req,
         identify_family::BuildModel::Response &res)
{
  FILE* cam_view = popen("rosrun image_view image_view image:=/image_raw","r");
  FILE* cam_open = popen("roslaunch identify_family usb_camera.launch 2>/dev/null","r");
  sleep(2);
  char cmd[300]; 
  sprintf(cmd,"rosrun identify_family take_photo_index.py _label:=%s _start:=%d _end:=%d",req.name.c_str(),(int)req.start,(int)req.end);
  system(cmd);

  system("pkill -f image_view");  
  FILE* cam_close = popen("rosnode kill /uvc_camera_node 2>/dev/null","w");
  pclose(cam_open);pclose(cam_close);pclose(cam_view);
  memset(cmd, 0, sizeof cmd);
//  char cmd[100]; 

  sprintf(cmd,"`rospack find identify_family`/openface_tool/util/align-dlib.py `rospack find identify_family`/mydataset/raw align outerEyesAndNose `rospack find identify_family`/mydataset/raw_aligned --size 96");
  system(cmd);
  memset(cmd, 0, sizeof cmd);

//  remove("`rospack find identify_family`/mydataset/raw_aligned/cache.t7");
  sprintf(cmd,"rm `rospack find identify_family`/mydataset/raw_aligned/cache.t7 -f");
  system(cmd);//block 
  memset(cmd, 0, sizeof cmd);


  sprintf(cmd,"`rospack find identify_family`/openface_tool/batch-represent/main.lua -outDir `rospack find identify_family`/my_models/openface -data `rospack find identify_family`/mydataset/raw_aligned");
  system(cmd);
  memset(cmd, 0, sizeof cmd);

  sprintf(cmd,"`rospack find identify_family`/openface_tool/demos/classifier.py train `rospack find identify_family`/my_models/openface");
  system(cmd);
  memset(cmd, 0, sizeof cmd);
  ROS_INFO("Build Model Finished! \n");
  res.status = "finished";
  return true;
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "build_model_srv");
  ros::NodeHandle n;

  ros::ServiceServer service = n.advertiseService("build_model_srv", build_model);
  ROS_INFO("Ready to Build Model.");
  ros::spin();

  return 0;
}
