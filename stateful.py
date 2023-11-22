#!/usr/bin/python

import math

angle_type = 'radians'

def cosecant(x):
    global angle_type
    if angle_type == 'radians':
        return 1/math.sin(x)
    elif angle_type == 'degrees':
        return 1/math.sin(x*math.pi/180)
    else:
        raise NotImplementedError('cosecant is not implemented for angle type', angle_type)


# result = cosecant(30)
print(cosecant(30))
