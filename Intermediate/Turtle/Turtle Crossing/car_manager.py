from turtle import Turtle
import random

# Define constants for car attributes and movement speed
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    """
    Manages the cars in the game. The CarManager class handles creating new cars, 
    moving them across the screen, and increasing their speed as the game progresses.
    """
    
    def __init__(self):
        """
        Initializes the CarManager. Sets up an empty list of cars and sets the 
        initial speed of the cars to the starting move distance.
        """
        self.all_cars = []  # List to store all the car objects
        self.car_speed = STARTING_MOVE_DISTANCE  # Initial car speed

    def create_car(self):
        """
        Randomly creates a new car and places it at a random vertical position 
        on the right side of the screen. The chance of creating a new car is 1 in 6.
        The car is assigned a random color from the predefined list of colors.
        """
        random_chance = random.randint(1, 6)  # Random chance to create a car (1 in 6)
        if random_chance == 1:  # 1 in 6 chance to create a car
            new_car = Turtle("square")  # Create a new square turtle for the car
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # Stretch the square to resemble a car
            new_car.penup()  # Lift the pen so the car doesn't draw
            new_car.color(random.choice(COLORS))  # Set a random color for the car
            random_y = random.randint(-250, 250)  # Set a random Y position
            new_car.goto(300, random_y)  # Place the car at the far right
            self.all_cars.append(new_car)  # Add the car to the list of all cars

    def move_cars(self):
        """
        Moves all cars in the list to the left by the current car speed. 
        This is called on each game loop to animate the cars.
        """
        for car in self.all_cars:
            car.backward(self.car_speed)  # Move each car backward by car_speed distance

    def level_up(self):
        """
        Increases the speed of the cars by the move increment. This method is called 
        when the player reaches the finish line, making the game progressively harder.
        """
        self.car_speed += MOVE_INCREMENT  # Increase the car speed by the defined increment
