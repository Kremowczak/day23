import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
car_manager = CarManager()
scoreboard = Scoreboard()
player = Player()
screen.onkeypress(player.move, "w")



scoreboard.draw_score()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
    if player.ycor() >= (FINISH_LINE_Y + 0):
        player.reset()
        scoreboard.level_up()
        car_manager.increase_speed()


    for car in car_manager.cars:
        if abs(car.xcor() - player.xcor()) < 27 and abs(car.ycor() - player.ycor()) < 22:
            game_is_on = False

screen.exitonclick()