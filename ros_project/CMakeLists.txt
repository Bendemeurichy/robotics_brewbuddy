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

# Include directories
include_directories(
  include
  ${OpenCV_INCLUDE_DIRS}
)

# Add executable
add_executable(detect_people src/detect_people.cpp)
ament_target_dependencies(detect_people rclcpp sensor_msgs cv_bridge OpenCV)
ament_target_dependencies(joystick_control rclcpp joy geometry_msgs)

# Install executable
install(TARGETS
  detect_people
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
