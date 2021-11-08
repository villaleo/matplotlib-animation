"""
Project: Mathematics 270 - Linear Algebra Animation Project
File: AnimationProject.py
Description: Plots an image and animates it using vectors, linear transformations,
             matrices, and other concepts taught throughout the linear algebra course.
Author: Leonardo Villalobos
"""

import matplotlib.pyplot as plot
from Objects import *
import math
import AnimationClass as Animate


def display_animation() -> None:
    # ------------------ Animation ------------------
    animated_grass = [Animate.Matrix(grass) for grass in grass_pieces]
    animated_horizon = Animate.Matrix(horizon)
    animated_flower_body = [Animate.Matrix(entry) for entry in body]
    animated_center = Animate.Matrix(center)
    animated_petals = [Animate.Matrix(petal) for petal in petals]
    animated_sun = [Animate.Matrix(ray) for ray in sun_rays]

    plot.ion()

    for i in range(0, 35):
        animated_grass[0].plot(tcolor='green')
        animated_grass[1].plot(0, tcolor='green')
        animated_horizon.plot(0, tcolor='green')

        for petal in animated_petals:
            petal.plot(0, tcolor='red')

        for part in animated_flower_body:
            part.plot(0, tcolor='green')

        animated_center.plot(0, tcolor='orange')

        for ray in animated_sun:
            ray.plot(0, tcolor='yellow')

        if i % 2 == 0:
            animated_grass[0].shear(0.3)
            animated_grass[0].translate(1.4, 0)

            animated_horizon.translate(0, 0.3)

            animated_grass[1].shear(0.3)
            animated_grass[1].translate(1, 0)

            for petal in animated_petals:
                petal.translate(0.2, 0)

            for part in animated_flower_body:
                part.translate(0.2, 0)

            animated_center.translate(0.2)

            for ray in animated_sun:
                ray.translate(0.2, 0)
                ray.rotate(math.pi / 4, about='center')
        else:
            animated_grass[0].shear(-0.3)
            animated_grass[0].translate(-1.4, 0)

            animated_horizon.translate(0, -0.3)

            animated_grass[1].shear(-0.3)
            animated_grass[1].translate(-1, 0)

            for petal in animated_petals:
                petal.translate(-0.2, 0)

            for part in animated_flower_body:
                part.translate(-0.2, 0)

            animated_center.translate(-0.2)

            for ray in animated_sun:
                ray.translate(-0.2, 0)

        plot.gcf().canvas.flush_events()
        plot.pause(.2)

    # ------------------ End Animation ------------------
