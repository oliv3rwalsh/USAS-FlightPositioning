# Overview
The USAS Flight Position Visualization program is a lightweight, modular Python program that uses the tkinter and matplotlib libraries. Both libraries are installed through the native pip interface integrated with all Python installations. The lightweight nature of the program and its relatively low memory requirements allow for compatibility with smaller processors. Additionally, more intensive software could be run in parallel as the program averages 80 MB of memory at a 200ms refresh rate.
# Functionality
The program visualizes an aerial system's position in 3D space relative to a fixed safe area using XZ and YZ graphs with variable bounds. The position of the aerial system can be read into the program using various methods, allowing for compatibility with external software. Presently, the 3D safe area is defined by a fixed point in space with a fixed radius, however, later versions could easily include variable safe area locations and more complex geometry. Note that if the reference frame is in motion, the recommendation is that the safe area remains fixed relative to the operator and that the position of the aerial system is adjusted accordingly.
# Customization and Modularity
The current version allows for customization of the bounds of the graphs, the refresh rate, and graph images. Python's wide range of compatible software allows for easy implementation of additional methods to update the aerial system and safe area locations. The current version of the program comes prefilled with a positioning method that randomly adjusts the location for testing purposes.

# Usage
The interface includes a top banner, two graphs, and a logo banner. The top banner's text reflects the current status of the aerial system, and the graphs update on each refresh (every 200ms by default).

### Case 1 - Contained by Safe Area
The top banner reads _Loiter OK_ when the system, represented by a black dot, is contained by the safe area, represented by a blue sphere. Note that the program allows for customization of the colors used for representation.
![Img 1](https://i.ibb.co/WVDZqSf/Screenshot-2024-08-17-235634.png)

### Case 2 - Outside Safe Area
The top banner will show the system's shortest distance from the 3D safe area when external to its bounds. Additionally, a dashed line extends 50% of the distance between the system and the center of the safe area. Note that the program allows for this distance to be adjusted.
![Img 2](https://i.ibb.co/MP5cFHV/Screenshot-2024-08-17-235739.png)
