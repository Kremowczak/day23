import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        if random.randint(1, 2) == 1:
            print("trying to spawn")
            for car in self.cars:
                if car.xcor() > 240:
                    print("blocked by car at", car.xcor())
                    return
            print("spawned!")
            self.cars.append(Car(self.car_speed))

    def move_cars(self):
        for car in self.cars[:]:
            if car.xcor() < -280:
                car.hideturtle()
                self.cars.remove(car)

            else:
                car.move()
    def increase_speed(self):
        for car in self.cars[:]:
            car.speed += MOVE_INCREMENT
        self.car_speed += MOVE_INCREMENT


class Car(Turtle):
    def __init__(self, speed):
        super().__init__()
        self.shape("square")
        color = random.choice(COLORS)
        self.color(color)
        self.penup()
        self.goto(280, random.randint(-260, 260))
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.speed = speed

    def move(self):
            self.forward(self.speed)