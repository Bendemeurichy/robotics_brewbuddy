cmake_minimum_required(VERSION 3.5)
project(robotics_brewbuddy)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(cv_bridge REQUIRED)
find_package(OpenCV REQUIRED)
find_package(joy REQUIRED)
find_package(slam_toolbox REQUIRED)
find_package(nav2_bringup REQUIRED)
find_package(speech_recognition REQUIRED)
find_package(textblob REQUIRED)

# Include directories
include_directories(
  include
  ${OpenCV_INCLUDE_DIRS}
)

# Add executable
add_executable(detect_people src/detect_people.cpp)
ament_target_dependencies(detect_people rclcpp sensor_msgs cv_bridge OpenCV)
ament_target_dependencies(joystick_control rclcpp joy geometry_msgs)
add_executable(audio_processing src/audio_processing.py)
ament_target_dependencies(audio_processing rclcpp speech_recognition std_msgs)
add_executable(sentiment_analysis src/sentiment_analysis.py)
ament_target_dependencies(sentiment_analysis rclcpp textblob std_msgs)
add_executable(llm_client src/llm_client.py)
ament_target_dependencies(llm_client rclcpp requests std_msgs)

# Install executable
install(TARGETS
  detect_people
  audio_processing
  sentiment_analysis
  llm_client
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
