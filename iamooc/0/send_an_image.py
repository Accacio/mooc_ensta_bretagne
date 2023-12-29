#!/usr/bin/env python3

from codac import *
from vibes import vibes
f = Function('x','y','1+cos(x)+sin(y)^2')
S = SepFwdBwd(f, [1,2])
X0 = IntervalVector(2,[-2,2])
vibes.beginDrawing()
SIVIA(X0,S,0.01)
vibes.axisAuto()
vibes.setFigureSize(500,500)

