from math import sqrt

class Rocket():
    """Rocket simulates a rocket ship for a game or a physics simulation."""
    
    def __init__(self, x=0, y=0):
        """Each rocket has an (x,y) position in 2D space."""
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        """Moves the rocket according to the paremeters given.
           Default behavior is to move the rocket up one unit."""
        self.x += x_increment
        self.y += y_increment
        
    def get_distance(self, other_rocket):
        """Calculates the distance from this rocket to another rocket,
           and returns that value"""
        distance = sqrt((self.x-other_rocket.x)**2+(self.y-other_rocket.y)**2)
        return distance
    
