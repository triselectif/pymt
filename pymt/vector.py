__docformat__ = 'restructuredtext'

import math

class Vector(object):
    '''Represents a 2D vector.

    '''
    __slots__ = ('x', 'y')
    def __init__(self, x = 0.0, y = 0.0):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, val):
        return Vector(self.x + val.x, self.y + val.y)

    def __sub__(self,val):
        return Vector(self.x - val.x, self.y - val.y)

    def __iadd__(self, val):
        self.x += val.x
        self.y += val.y
        return self

    def __isub__(self, val):
        self.x -= val.x
        self.y -= val.y
        return self

    def __div__(self, val):
        return Vector(self.x / val, self.y / val)

    def __mul__(self, val):
        return Vector(self.x * val, self.y * val )

    def __idiv__(self, val):
        self.x = self.x / val
        self.y = self.y / val
        return self

    def __imul__(self, val):
        self.x = self.x * val
        self.y = self.y * val
        return self

    def __str__(self):
        return '(%.1f,%.1f)' % (self.x, self.y)

    def length(self):
        return Vector.length(self)

    def normalized(self):
        l = length(self)
        return Vector(self.x /l , self.y / l)

    @staticmethod
    def distanceSqrd(vec1, vec2):
        """Returns the distance between two points squared.
        Marginally faster than Distance()
        """
        return ((vec1.x - vec2.x)**2 + (vec1.y - vec2.y)**2)

    @staticmethod
    def distance(vec1, vec2):
        """Returns the distance between two points"""
        return math.sqrt(Vector.distanceSqrd(vec1, vec2))

    @staticmethod
    def lengthSqrd(vec):
        """Returns the length of a vector sqaured.
        Faster than Length(), but only  marginally"""
        return vec.x**2 + vec.y**2

    @staticmethod
    def length(vec):
        'Returns the length of a vector'
        return math.sqrt(Vector.lengthSqrd(vec))

    @staticmethod
    def normalized(vec):
        'Returns the length of a vector'
        return math.sqrt(Vector.lengthSqrd(vec))

    @staticmethod
    def normalize(vec):
        """Returns a new vector that has the same direction as vec,
        but has a length of one."""
        if vec.x == 0. and vec.y == 0.:
            return Vector(0.,0.)
        return vec / Vector.length(vec)

    @staticmethod
    def dot(vec1, vec2):
        'Computes the dot product of a and b'
        return vec1.x * vec2.x + vec1.y * vec2.y

    @staticmethod
    def angle(v1, v2):
        'Computes the angle between a and b'
        angle = -(180/math.pi)*math.atan2(v1.x*v2.y - v1.y*v2.x, v1.x*v2.x+v1.y*v2.y)
        return angle

    @staticmethod
    def line_intersection(v1,v2, v3, v4):
        """
        finds the intersection point between the lines (1)v1->v2 and (2)v3->v4
        and returns it as a vector object

        for math see: http://en.wikipedia.org/wiki/Line-line_intersection
        """
        #linear algebar sucks...seriously!!
        x1,x2,x3,x4 = float(v1.x), float(v2.x), float(v3.x), float(v4.x)
        y1,y2,y3,y4 = float(v1.y), float(v2.y), float(v3.y), float(v4.y)

        u = (x1*y2-y1*x2)
        v = (x3*y4-y3*x4)
        denom = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
        if denom == 0:
            return None

        px = ( u*(x3-x4) - (x1-x2)*v ) / denom
        py = ( u*(y3-y4) - (y1-y2)*v ) / denom

        return Vector(px,py)





import operator
from numpy import matrix

def matrix_inv_mult(m, v):
    """  takes an openGL matrix and a 2 Vector and returns the inverse of teh matrix applied to the vector """
    mat = matrix(
        [[m[0],m[1],m[2],m[3]],
         [m[4],m[5],m[6],m[7]],
         [m[8],m[9],m[10],m[11]],
         [m[12],m[13],m[14],m[15]]] )
    vec = matrix(v)
    inv = mat.I
    result = vec*inv
    return Vector(result[0,0],result[0,1])

def matrix_trans_mult(m, v):
    """  takes an openGL matrix and a 2 Vector and returns the transpose of teh matrix applied to the vector """
    mat = [[m[0],m[4],m[8],m[12]],
         [m[1],m[5],m[9],m[13]],
         [m[2],m[6],m[10],m[14]],
         [m[3],m[7],m[11],m[15]]]
    vec = matrix(v)
    result = vec*mat
    return Vector(result[0,0],result[0,1])

def matrix_mult(m, v):
    """  takes an openGL matrix and a 2 Vector and returns the matrix applied to the vector """
    mat = [[m[0],m[1],m[2],m[3]],
         [m[4],m[5],m[6],m[7]],
         [m[8],m[9],m[10],m[11]],
         [m[12],m[13],m[14],m[15]]]
    vec = matrix(v)
    result = vec*mat
    return Vector(result[0,0],result[0,1])
