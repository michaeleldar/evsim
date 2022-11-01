#!/usr/local/bin/python3
from creature import Creature
import turtle
from time import sleep

creature = Creature()
creature_gui = turtle.Turtle()
creature_gui.goto(0, 0)
creature_gui.shape("circle")
creature_gui.forward(100)
sleep(5)
