#include "ros/ros.h"
#include "identify_family/FaceRec.h"
#include <cstdlib>
#include "std_msgs/String.h"
#include "std_msgs/UInt8.h"
#include <sstream>
#include <iostream>
#include <string>
int flag=0;
void srvCallback(const std_msgs::UInt8::ConstPtr& msg)
{
  flag=msg->data;//1
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "face_rec_client_android");
  ros::NodeHandle n;
  ros::Subscriber srv_sub = n.subscribe("andbot_face_rec_srv/start", 1000, srvCallback);
  ros::Publisher person_pub = n.advertise<std_msgs::String>("andbot_face_rec_srv/anwser", 1000);
  ros::ServiceClient client = n.serviceClient<identify_family::FaceRec>("face_rec_srv");
  identify_family::FaceRec srv;
  srv.request.request = "";

  ros::Rate r(10); // 10 hz
  while (ros::ok())
  {
	if (flag==1){
	  if (client.call(srv))
	  {
		ROS_INFO("Call service");
		flag=0;
		std::cout<<"the anwser is "<< srv.response.anwser<<std::endl;
		std_msgs::String msg;

		std::stringstream ss;
		ss << srv.response.anwser;
		msg.data = ss.str();
    	person_pub.publish(msg);
	  }
	  else
	  {
		ROS_ERROR("Failed to call service");
		return 1;
	  }
	}
    ros::spinOnce();
    r.sleep();
  }

  return 0;
}
