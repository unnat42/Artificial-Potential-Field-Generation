# Artificial-Potential-Field-Generation
Generate a potential field over an image with obstacles 

Artificial Potential Field is one of many algorithms that can be used for path planning for robotics. It includes, as the name suggests, a mathematical potential function for the given map which is formulated in a way that it makes the potential for initial position high and final position as the least and applying gradient descent ensures the movement of our bot from high potential to lower potential i.e., initial position to final or goal position. 

This function comprises of 2 potential functions namely attractive potential and repulsive. The attractive potential function attracts the bot towards the potential whereas repulsive potential is applied on obstacles and generates repulsion of bot from the obstacles to make sure collision doesnt occur. 

In this code, quadratic function is applied for attractive function and a single scalar value for repulsive. Cubic function is also provided for the attractive function in the comments. A quadratic function can be used for repulsive function as well. 
