cmake_minimum_required(VERSION 3.5)
project(iai_pr2_description)

find_package(ament_cmake REQUIRED)

# Install launch files
install(DIRECTORY launch/
  DESTINATION share/${PROJECT_NAME}/launch
)

# Install robot description files
install(DIRECTORY robots/
  DESTINATION share/${PROJECT_NAME}/robots
)

# Install robot description files
install(DIRECTORY meshes/
  DESTINATION share/${PROJECT_NAME}/meshes
)

# Install robot description files
install(DIRECTORY sensors/
  DESTINATION share/${PROJECT_NAME}/sensors
)

ament_package()
