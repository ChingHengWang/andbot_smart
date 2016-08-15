#include "ros/ros.h"
#include "identify_family/FaceRec.h"
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <string>
#include <iostream>
#include <vector>
#include <map>
#include <string>
#include "../lib/inih/cpp/INIReader.h"
using namespace std;
string ini_path = "/home/zach/catkin_ws/src/andbot_smart/identify_family/srv.ini";
INIReader reader(ini_path);
const string INI_PKG_FOLDER = reader.Get("face_rec_srv","pkg_folder","UNKNOW");

int message1= 0;
int message2= 1;
int message3= 2;

vector<string> pv;
map<string,int> pm;

void *classify_funciton(void* index){
  int idx=*((int*)index);
  printf ("pthread %d start classify\n",idx);
  string data;
  stringstream ss;
  char buffer[300];
  char cmdtmp[300]; 
//debug  cout <<"TESTING !!!"<< pkg_path <<endl;

  sprintf(cmdtmp,"%s/openface_tool/demos/classifier.py infer %s/my_models/openface/classifier.pkl %s/photo/test/unknow/image-%d.jpg 2>/dev/null",INI_PKG_FOLDER.c_str(),INI_PKG_FOLDER.c_str(),INI_PKG_FOLDER.c_str(),idx);
  FILE *fd = popen(cmdtmp, "r");
  while(!feof(fd)) {
	if (fgets(buffer, 300, fd) !=NULL)
		data.append(buffer);
  }
  ss<<data;
//  cout <<"test "<<data<<endl;
  string tmp_name,tmp;
  double tmp_score=0.0;
  while( ss>>tmp_name && tmp_name.compare("Predict")) ;
  ss>>tmp_name; ss>>tmp; ss>>tmp_score;
  if (!tmp_name.compare("==="))
	tmp_name="none";
  pv.push_back(tmp_name); 
//  cout <<"test "<<tmp<<endl;
  printf ("pthread %d anwser is %s score %f\n",idx,tmp_name.c_str(),tmp_score);

}



bool face_rec(identify_family::FaceRec::Request  &req,
         identify_family::FaceRec::Response &res)
{
  ROS_INFO("Start face_rec service\n");
  //clear person memory
  pv.clear(); pm.clear();

  char cmd[300]; 
  sprintf(cmd,"rm %s/photo/test/unknow/* -fr",INI_PKG_FOLDER.c_str());
  system(cmd);//block 
  memset(cmd, 0, sizeof cmd);

  FILE* view_open = popen("rosrun image_view image_view image:=/image_raw","r");
  FILE* cam_open = popen("roslaunch identify_family usb_camera.launch 2>/dev/null","r");
  sleep(5);
  system("rosrun identify_family take_photo_cap.py");//block 
/*
  sprintf(cmd,"`rospack find identify_family`/openface_tool/util/align-dlib.py `rospack find identify_family`/photo/test align outerEyesAndNose `rospack find identify_family`/photo/test_aligned --size 96");
  system(cmd); 
  memset(cmd, 0, sizeof cmd);
*/
  FILE* view_close = popen("pkill -f image_view 1>/dev/null","w");  
  FILE* cam_close = popen("rosnode kill /uvc_camera_node 1>/dev/null","w");
  pclose(cam_open);pclose(cam_close);pclose(view_open);pclose(view_close);

  pthread_t thread1,thread2,thread3;
  pthread_create(&thread1, NULL , classify_funciton ,(void*)&message1);
  pthread_create(&thread2, NULL , classify_funciton ,(void*)&message2);
  pthread_create(&thread3, NULL , classify_funciton ,(void*)&message3);

  pthread_join( thread1, NULL);
  pthread_join( thread2, NULL);
  pthread_join( thread3, NULL);

  for (int i=0; i<pv.size();i++)
  {
    map<string,int>::iterator it = pm.find(pv[i]);
	if (it == pm.end()) 
		pm.insert(pair<string,int>(pv[i],1));
	else 
		pm[pv[i]]+=1;
  }  	  
  map<string,int>::iterator it = pm.begin();
  for (map<string,int>::iterator it2 = pm.begin(); it2 != pm.end(); ++it2)
  {
    if (it2->second > it->second)
		it=it2;
  } 
  string anwser = it->first;  
  printf("final anwser is %s\n",anwser.c_str());
  res.anwser=anwser; 
  ROS_INFO("Face Rec Finished! \n");

  
  return true;
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "face_rec_srv");
  ros::NodeHandle n;

  if (reader.ParseError() < 0) {
	  std::cout << "Can't load 'srv.ini'\n";
	 return 1;
  }

  ros::ServiceServer service = n.advertiseService("face_rec_srv", face_rec);
  ROS_INFO("Ready to Face Rec.");
  ros::spin();

  return 0;
}
