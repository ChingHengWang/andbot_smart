# identify_family


* cp inih_pkg/lib ~/catkin_ws/src/identify_family/ -r
* cp inih_pkg/3d_party/inih ~/catkin_ws/src/identify_family/3d_party/ -r

* edit CMakeLists.txt

		file(GLOB_RECURSE SRCS
			"lib/*.cpp"
			"lib/*.c"
		)
		file(GLOB_RECURSE HDRS
			"lib/*.h"
		)
		add_executable(face_rec_srv src/face_rec_srv.cpp ${SRCS} ${HDRS})


* add include file

		#include "../lib/inih/cpp/INIReader.h"

		#include <iostream>

* add code 

		INIReader reader("/home/zach/catkin_ws/src/identify_family/srv.ini");

		  if (reader.ParseError() < 0) {
		      std::cout << "Can't load 'srv.ini'\n";
		     return 1;
		  }
* catkin_make -j4 success!

