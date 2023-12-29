# [[file:CH1.org::*Test][Test:1]]
from myinterval import *

x = Interval(-1,3)
y = Interval(2,5)
print(x,"+",y,"="        ,Interval_sum(x,y))
print(x,"-",y,"="        ,Interval_sub(x,y))
print(x,"·",y,"="        ,Interval_mul(x,y))
print(x,"/",y,"="        ,Interval_div(x,y))
print("max(",x,",",y,")=",Interval_max(x,y))
print("min(",x,",",y,")=",Interval_min(x,y))
# Test:1 ends here
