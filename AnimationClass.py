"""
Project: Mathematics 270 - 2d Animations
File: AnimationClass.py
Description: Module containing the class of MatrixObjects and linear transformation (defined via methods)
Author: Dr. Greg Rainwater
"""

import matplotlib.pyplot as plt
import numpy as np
import math


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        onesRow = np.ones(self.matrix.shape[1])
        self.matrix = np.vstack((self.matrix, onesRow))

    def rotate(self, radians, about='origin'):
        cos_t = math.cos(radians)
        sin_t = math.sin(radians)
        if about == 'origin':
            self.matrix = np.matrix(' %s %s  0;'
                                    ' %s %s  0;'
                                    '  0  0  1' % (cos_t, -sin_t, sin_t, cos_t)) * self.matrix
        elif about == 'point':
            xpoint = self.matrix[0, 0]
            ypoint = self.matrix[1, 0]
            self.translate(-xpoint, -ypoint)
            self.matrix = np.matrix(' %s %s  0;'
                                    ' %s %s  0;'
                                    '  0  0  1' % (cos_t, -sin_t, sin_t, cos_t)) * self.matrix
            self.translate(xpoint, ypoint)

        elif about == 'center':
            xpoint = np.mean(self.matrix[0, :])
            ypoint = np.mean(self.matrix[1, :])
            self.translate(-xpoint, -ypoint)
            self.matrix = np.matrix(' %s %s  0;'
                                    ' %s %s  0;'
                                    '  0  0  1' % (cos_t, -sin_t, sin_t, cos_t)) * self.matrix
            self.translate(xpoint, ypoint)

    def translate(self, dx=0, dy=0):
        self.matrix = np.matrix(' 1  0 %s;'
                                ' 0  1 %s;'
                                ' 0  0  1' % (dx, dy)) * self.matrix

    def scale(self, dx=1, dy=1):
        self.matrix = np.matrix('%s  0  0;'
                                ' 0 %s  0;'
                                ' 0  0  1' % (dx, dy)) * self.matrix

    def reflect(self, axis='x', about='origin'):
        if about == 'point':
            xpoint = self.matrix[0, 0]
            ypoint = self.matrix[1, 0]
        else:
            xpoint = 0
            ypoint = 0
        self.translate(-xpoint, -ypoint)
        if axis == 'x':
            self.matrix = np.matrix(' 1  0  0; '
                                    ' 0 -1  0; '
                                    ' 0  0  1') * self.matrix
        elif axis == 'y':
            self.matrix = np.matrix('-1  0  0; '
                                    ' 0  1  0; '
                                    ' 0  0  1') * self.matrix
        elif axis == 'xy':
            self.matrix = np.matrix(' 0  1  0; '
                                    ' 1  0  0; '
                                    ' 0  0  1') * self.matrix
        elif axis == 'nxy':
            self.matrix = np.matrix('-1  0  0; '
                                    ' 0 -1  0; '
                                    ' 0  0  1') * self.matrix

        self.translate(xpoint, ypoint)

    def shear(self, dx=0, dy=0):
        self.matrix = np.matrix(' 1 %s  0; '
                                '%s  1  0; '
                                ' 0  0  1' % (dx, dy)) * self.matrix

    def putOrigin(self):
        xpoint = self.matrix[0, 0]
        ypoint = self.matrix[1, 0]
        self.translate(-xpoint, -ypoint)

    #    def plot(self, clrfig=1,xMin=-5,xMax=30,yMin=-5,yMax=30):
    def plot(self, clrfig=1, xMin=-20, xMax=20, yMin=-20, yMax=20, tcolor=''):
        if clrfig == 1:
            plt.gcf().clear()
        if tcolor == '':
            plt.plot(np.transpose(self.matrix[0, :]), np.transpose(self.matrix[1, :]))
        else:
            plt.plot(np.transpose(self.matrix[0, :]), np.transpose(self.matrix[1, :]), color=tcolor)
        plt.xlim(xMin, xMax)
        plt.ylim(yMin, yMax)
        plt.show()

    def plot2(self, clrfig=1, pxlim=100, pylim=100, tcolor=''):
        if clrfig == 1:
            plt.gcf().clear()
        # plt.gcf().clear()
        if tcolor == '':
            plt.plot(np.transpose(self.matrix[0, :]), np.transpose(self.matrix[1, :]))
        else:
            plt.plot(np.transpose(self.matrix[0, :]), np.transpose(self.matrix[1, :]), color=tcolor)
        plt.xlim(0, pxlim)
        plt.ylim(0, pylim)
        plt.show()
