"""
Project: Mathematics 270 - Starter Code for 2d Animations
File: 2dAnimationStartCodeBlank.py
Description: For creating objects and performing the animations.  
             The linear transformations must be defined in the module "AnimationClassStudents.py" 
Author: Dr. Greg Rainwater
"""

import matplotlib.pyplot as plot
import numpy as np
import math
import AnimationClass as Animate


def main():
    """
    ------------------------------------------------------
    Create Your Object(s)
        Store the vertices of the object in a 2 x n matrix where
        the x coordinates of the vertices are stored in first row and
        the y coordinates in the second row.
        Each successive pair of points is connected by a straight line.
    ---
    EXAMPLE:
    ---
    Consider the parallelogram formed by the vertices (2,0), (1,2), (2,4)
    and (3,2). Form Object matrix using vertices as columns and adding starting
    vector (2,0) onto tail/end (otherwise we would be missing a line) is
        M=( 2 1 2 3 2; 0, 2, 4, 2 0)
        M=np.matrix('2 1 2 3 2; 0, 2, 4, 2 0')
        Obj1= Ani.Matrix(M)
    ------------------------------------------------------
    """

    # Objects
    grass_pieces = [
        np.matrix(
            '-4 -4.9 -6.3 -6.7 -7 -7.4 -9 -9.2 -10 -9.2 -9 -7.4 -7 -6.7 -6.3 -4.9 -4;'
            '-4.3 -2.9 -3.1 -2.8 -1.3 -1.2 -2.4 -2 -4 -2 -2.4 -1.2 -1.3 -2.8 -3.1 -2.9 -4.3'
        ),
        np.matrix(
            '2.2 4.7 5.4 6.9 10 6.9 5.4 4.7 2.2;'
            '-8 -6 -6.5 -5.4 -4.6 -5.4 -6.5 -6 -8'
        )
    ]

    horizon = np.matrix(
        '-10 -7.6 -6.4 -5.3 -4.2 -1.9 -1 1.5 4.9 7.1 9.6 10 9.6 7.1 4.9 1.5 -1 -1.9 -4.2 -5.3 -6.4 -7.6 -10;'
        '0.2 0.5 0.6 0.9 0.9 1 0.8 1.1 0.8 1.2 0.6 0.8 0.6 1.2 0.8 1.1 0.8 1 0.9 0.9 0.6 0.5 0.2'
    )

    stem = np.matrix(
        '-0.2 0.2 0.1 -0.7 -0.8;'
        '-1 -0.4 0.2 1 1.6'
    )
    leaves = [
        np.matrix(
            '-0.22 0 0.3 0 -0.22;'
            '0.52 0.7 0.64 0.5 0.52'
        ),
        np.matrix(
            '0.15 -0.1 0.2;'
            '-0.1 0.1 -0.4'
        )
    ]

    center = np.matrix(
        '-1 -0.7 -0.4 -0.4 -0.7 -1 -1.1 -1;'
        '1.5 1.4 1.6 1.8 1.9 2 1.8 1.5'
    )

    petals = [
        np.matrix(
            '-1 -1.4 -1;'
            '2 2.5 2'
        ),
        np.matrix(
            '-0.7 -0.5 -0.7;'
            '1.9 2.5 1.9'
        ),
        np.matrix(
            '-0.4 0.1 -0.4;'
            '1.8 2.2 1.8'
        ),
        np.matrix(
            '-0.4 0.1 -0.4;'
            '1.6 1.4 1.6'
        ),
        np.matrix(
            '-0.7 -0.5 -0.7;'
            '1.4 1 1.4'
        ),
        np.matrix(
            '-1 -1.5 -1;'
            '1.5 1.3 1.5'
        ),
        np.matrix(
            '-1.1 -1.6 -1.1;'
            '1.8 1.9 1.8'
        )
    ]

    # Animation
    animated_grass = [
        Animate.Matrix(grass_pieces[0]),
        Animate.Matrix(grass_pieces[1])
    ]
    animated_horizon = Animate.Matrix(horizon)
    animated_flower_body = [
        Animate.Matrix(stem),
        Animate.Matrix(leaves[0]),
        Animate.Matrix(leaves[1])
    ]
    animated_center = Animate.Matrix(center)
    animated_petals = [
        Animate.Matrix(petals[0]),
        Animate.Matrix(petals[1]),
        Animate.Matrix(petals[2]),
        Animate.Matrix(petals[3]),
        Animate.Matrix(petals[4]),
        Animate.Matrix(petals[5]),
        Animate.Matrix(petals[6])
    ]

    plot.ion()

    for i in range(0, 20):
        animated_grass[0].plot(tcolor='green')
        animated_horizon.plot(0, tcolor='green')
        animated_grass[1].plot(0, tcolor='green')

        for petal in animated_petals:
            petal.plot(0, tcolor='red')

        for part in animated_flower_body:
            part.plot(0, tcolor='green')

        animated_center.plot(0, tcolor='orange')

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

        plot.gcf().canvas.flush_events()
        plot.pause(.2)
