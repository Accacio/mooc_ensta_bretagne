from codac import *
from vibes import vibes
f = Function('x','y','x*cos(x-y)+y')
S = SepFwdBwd(f, [1,2])
X0 = IntervalVector(2,[-2,2])
vibes.beginDrawing()
SIVIA(X0,S,0.01)
vibes.axisAuto()
vibes.setFigureSize(500,500)
vibes.saveImage('helloIntervals.jpg')
vibes.endDrawing()
