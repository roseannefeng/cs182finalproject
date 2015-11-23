from copy import deepcopy
import timeit
import sys, os
import random 
import argparse
import heapq



#helper function that transposes matrix in order to make reassignment easier
def transpose(matrix):
    trmatrix = [[row[0] for row in matrix],[row[1] for row in matrix],  [row[2] for row in matrix]]
    return trmatrix

ultimate_list = []


class Cube:
    def __init__(self):

        self.fUp = [['Y', 'Y', 'Y'],
                    ['Y', 'Y', 'Y'],
                    ['Y', 'Y', 'Y']]
        self.fDown = [['W', 'W', 'W'],
                        ['W', 'W', 'W'],
                        ['W', 'W', 'W']]
        self.fLeft = [['R', 'R', 'R'],
                        ['R', 'R', 'R'],
                        ['R', 'R', 'R']]
        self.fRight = [['O', 'O', 'O'],
                        ['O', 'O', 'O'],
                        ['O','O','O']]
        self.fFront = [['G','G','G'],
                        ['G', 'G', 'G'],
                        ['G', 'G', 'G']]
        self.fBack = [['B', 'B', 'B'],
                        ['B', 'B', 'B'],
                        ['B', 'B', 'B']]
        # note: in functions that call face, functions will access the copy on state,
        # not the faces stored in the model itself


    def currentState(self):
        """ 
        Returns copy of state.
        Changes made to this do not affect the stored faces.
        """
        return [deepcopy(face) for face in 
            [self.fUp, self.fDown, self.fLeft, self.fRight, self.fFront, self.fBack]]

    def rotate90(self, state, face):
        """
        Rotates given face (int 0 through 5) on the state by
        90 degrees clockwise looking directly on face.
        Returns state', does not modify state or cube.
        """

        ultimate_list.append(face)
        up, down, left, right, front, back = [deepcopy(f) for f in state]

        # up = self.fUp
        # down = self.fDown
        # left = self.fLeft
        # right = self.fRight
        # front = self.fFront
        # back = self.fBack

        # IF FACE IS UP (UP AND DOWN DONT CHANGE)
        if face == 0:
            """
            temp = self.fFront[0]
            self.fFront[0] = self.fRight[0]
            self.fRight[0] = self.fBack[0]
            self.fBack[0] = self.fLeft[0]
            self.fLeft[0] = temp
            """
            temp = front
            front[0] = right[0]
            right[0] = back[0]
            back[0] = left[0]
            left[0] = temp

        # IF FACE IS DOWN (UP AND DOWN DONT CHANGE)
        elif face == 1:
            """
            temp = self.fFront[2]
            self.fFront[2] = self.fLeft[2]
            self.fLeft[2] = self.fBack[2]
            self.fBack[2] = self.fRight[2]
            self.fRight[2] = temp
            """
            temp = front[2]
            front[2] = left[2]
            left[2] = back[2]
            back[2] = right[2]
            right[2] = temp

        # IF FACE IS LEFT (LEFT AND RIGHT DONT CHANGE)
        elif face == 2:
            """
            relevant_matrices = [self.fFront, self.fDown, self.fBack, self.fUp]
            for i in relevant_matrices:
                i = transpose(i)

            temp = self.fFront[0]
            self.fFront[0] = self.fUp[0]
            self.fUp[0] = self.fBack[0]
            self.fBack[0] = self.fDown[0]
            self.fDown[0] = temp

            for ind, i in enumerate(relevant_matrices):
                i = transpose(i)

                if ind == 0:
                    self.fFront = i
                if ind == 1:
                    self.fDown = i
                if ind == 2:
                    self.fBack = i
                if ind == 3:
                    self.fUp = i
            """
            relevant_matrices = [front, down, back, up]
            for i in relevant_matrices:
                i = transpose(i)

            temp = front[0]
            front[0] = up[0]
            up[0] = back[0]
            back[0] = down[0]
            down[0] = temp

            for ind, i in enumerate(relevant_matrices):
                i = transpose(i)

                if ind == 0:
                    front = i
                if ind == 1:
                    down = i
                if ind == 2:
                    back = i
                if ind == 3:
                    up = i


        # IF FACE IS RIGHT (LEFT AND RIGHT DONT CHANGE)
        elif face == 3:
            """
            relevant_matrices = [self.fFront, self.fDown, self.fBack, self.fUp]
            for i in relevant_matrices:
                i = transpose(i)
            temp = self.fFront[2]
            self.fFront[2] = self.fDown[2]
            self.fDown[2] = self.fBack[2]
            self.fBack[2] = self.fUp[2]
            self.fUp[2] = temp

            for ind, i in enumerate(relevant_matrices):
                i = transpose(i)

                if ind == 0:
                    self.fFront = i
                if ind == 1:
                    self.fDown = i
                if ind == 2:
                    self.fBack = i
                if ind == 3:
                    self.fUp = i
            """
            relevant_matrices = [front, down, back, up]
            for i in relevant_matrices:
                i = transpose(i)
            temp = front[2]
            front[2] = down[2]
            down[2] = back[2]
            back[2] = up[2]
            up[2] = temp

            for ind, i in enumerate(relevant_matrices):
                i = transpose(i)

                if ind == 0:
                    front = i
                if ind == 1:
                    down = i
                if ind == 2:
                    back = i
                if ind == 3:
                    up = i

        # IF FACE IS FRONT (FRONT AND BACK DONT CHANGE)
        elif face == 4:
            """
            relevant_matrices = [self.fLeft, self.fDown, self.fRight, self.fUp]
            for i in relevant_matrices:
                i = transpose(i)
            temp = self.fLeft[2]
            self.fLeft[2] = self.fDown[2]
            self.fDown[2] = self.fRight[2]
            self.fRight[2] = self.fUp[2]
            self.fUp[2] = temp

            for ind, i in enumerate(relevant_matrices):
                i = transpose(i)

                if ind == 0:
                    self.fLeft = i
                if ind == 1:
                    self.fDown = i
                if ind == 2:
                    self.fRight = i
                if ind == 3:
                    self.fUp = i
            """
            relevant_matrices = [left, down, right, up]
            for i in relevant_matrices:
                i = transpose(i)
            temp = left[2]
            left[2] = down[2]
            down[2] = right[2]
            right[2] = up[2]
            up[2] = temp

            for ind, i in enumerate(relevant_matrices):
                i = transpose(i)

                if ind == 0:
                    left = i
                if ind == 1:
                    down = i
                if ind == 2:
                    right = i
                if ind == 3:
                    up = i

        # IF FACE IS BACK (FRONT AND BACK DONT CHANGE)
        elif face == 5:
            """
            relevant_matrices = [self.fLeft, self.fDown, self.fRight, self.fUp]
            for i in relevant_matrices:
                i = transpose(i)
            temp = self.fLeft[0]
            self.fLeft[0] = self.fUp[0]
            self.fUp[0] = self.fRight[0]
            self.fRight[0] = self.fDown[0]
            self.fDown[0] = temp

            for ind, i in enumerate(relevant_matrices):
                i = transpose(i)

                if ind == 0:
                    self.fLeft = i
                if ind == 1:
                    self.fDown = i
                if ind == 2:
                    self.fRight = i
                if ind == 3:
                    self.fUp = i
            """
            relevant_matrices = [left, down, right, up]
            for i in relevant_matrices:
                i = transpose(i)
            temp = left[0]
            left[0] = up[0]
            up[0] = right[0]
            right[0] = down[0]
            down[0] = temp

            for ind, i in enumerate(relevant_matrices):
                i = transpose(i)

                if ind == 0:
                    left = i
                if ind == 1:
                    down = i
                if ind == 2:
                    right = i
                if ind == 3:
                    up = i

        newState = [up, down, left, right, front, back]
        return newState



    def rotate(self, state, face, deg):
        """
        Rotates given face on the state by deg, which is an int 1, 2, or 3, by calling
        rotate90 deg times. Returns state', does not modify state or cube.
        """

        for i in range(deg):
            state = self.rotate90(state, face)
        return state

    def scramble(self, k):
        """
        Scrambles cube by calling k rotate functions which select a face and degree
        over a uniform random distribution. Modifies cube faces.
        """

        currentState = self.currentState()
        for i in range(k):

            face = random.randint(0, 5)
            degree = random.randint(1, 3)


            currentState = self.rotate(currentState, face, degree)

        print "scrambled {} times:".format(k), currentState
        #self.update(currentState)

    def numConflicts(self, state, face):
        """
        Returns the number of squares on face that differ from their initial color.
        Note: in a 3x3 cube, this value will range from 1 to 8 because center square
        in a cube cannot move.
        """
        return

    def fGoal(self, state, face):
        """
        Returns True if face is a solid color.
        """
        return

    def goal(self, state):
        """ 
        Returns True if all faces are a solid color.
        """
        return

    def update(self, state):
        """
        Given state, update the faces of the model accordingly.
        """
        return

our_cube = Cube()
print "initial:", our_cube.currentState()
our_cube.scramble(10)


# THIS JUST PRINTS THE ORDER IN WHICH FACES WERE ROTATED
# THE REVERSE ORDER IS THE SOLUTION TO THE PROBLEM WHICH 
# WILL BE USEFUL FOR CHECKING OUR SOLUTION

# print ultimate_list