# Overview
The USAS Flight Position Visualization program is a lightweight, modular python program that uses the tkinter and matplotlib libraries. Both libraries are easily installed through the native pip interface that ships with all python installations. The relatively low memory requirements (~80mb @ 200ms refresh) enable this software to be loaded onto smaller processors such as Raspberry Pis and allow for more intensive software to be run in parallel.
# Functionality
The program visualizes an aerial system's position in 3D space relative to a fixed safe area using XZ and YZ graphs with variable bounds. The position of the aerial system can be read into the program using a variety of methods, allowing for compatability with external software. Presently, the 3D safe area is represented by a fixed point in space with a fixed radius, however later version could easily include variable safe area locations and more complex geometry. Note that if the reference frame is in motion, it is recommended that the safe area remains fixed relative to the operator and that the position of the aerial system is interpreted/adjusted accordingly
# Customization and Modularity
The current version allows for customization of the bounds of the graphs, the refresh rate, and graph images. Python's wide range of compatible software allows for easy implementation of additional methods to update the aerial system and safe area locations. The current version of the program comes prefilled with a positioning method that randomly adjusts the location for testing purposes.

# Usage
The interface includes a top banner, two graphs, and a logo banner. The top banner's text reflects the current status of the aerial system and the graphs are updated on each refresh (defaults to 200ms)

### Case 1 - Contained by Safe Area
The top banner reads _Loiter OK_ when the system, represented by a black dot, is contained by the safe area, represented by a blue sphere. Note that the colors of each representation can be modified.
![Img 1](https://i.ibb.co/WVDZqSf/Screenshot-2024-08-17-235634.png)

### Case 2 - Outside Safe Area
The top banner will show the systems shortest distance from the 3D safe area when it is found to be outside of its bounds. Additionally, a dashed line is shown between the system and the center of the safe area that increases proportionally to the systems distance from the centerpoint. By default, this line extends 50% of the distance, however this can also be modified.
![Img 2](https://i.ibb.co/MP5cFHV/Screenshot-2024-08-17-235739.png)
