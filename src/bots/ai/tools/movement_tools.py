from langchain.tools import tool

from javascript import require, On, Once, AsyncTask, once, off

mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')

print(pathfinder)

@tool
def move_to_point_XYZ(x_coord : int, y_coord : int, z_coord : int):
    """Move to a specific point, used when there is a specified y coordinate.
    Args:
        x_coord (int): X coordinate of the point.
        y_coord (int): Y coordinate of the point.
        z_coord (int): Z coordinate of the point.
        """