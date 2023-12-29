# [[file:CH1.org::*Definition][Definition:1]]
import math

class Interval:
    def __init__(self,lb=-float("inf"),ub=float("inf")):
        self.lb = lb
        self.ub = ub

    def __str__(self):
        if math.isnan(self.lb) or math.isnan(self.ub):
            return "∅"
        else:
            if not math.isinf(self.lb):
                lb_str = str(self.lb)
            else:
                if self.lb<0:
                    lb_str = "-∞"
                else:
                    lb_str = "∞"
            if not math.isinf(self.ub):
                ub_str = str(self.ub)
            else:
                if self.ub<0:
                    ub_str = "-∞"
                else:
                    ub_str = "∞"
            return "[" + lb_str + "," + ub_str + "]"

    def __contains__(self,value):
        return value>=self.lb and value<=self.ub

empty_Interval = Interval(float("nan"),float("nan"))

def minimal_Interval(values:list):
    return Interval(min(values),max(values))

def Interval_sum(first:Interval,second:Interval):
    return Interval(first.lb+second.lb,first.ub+second.ub)

def Interval_sub(first:Interval,second:Interval):
    return Interval(first.lb-second.ub,first.ub-second.lb)

def Interval_mul(first:Interval,second:Interval):
    values = [first.lb*second.lb, first.lb*second.ub, first.ub*second.lb, first.ub*second.ub]
    return minimal_Interval(values)

def Interval_div(first:Interval,second:Interval):
    if 0 not in second:
        new_second = Interval(1/second.ub,1/second.lb)
    else:
        if second.ub==0:
            new_second = Interval(-float("inf"),1/second.lb)
        elif second.lb==0:
            new_second = Interval(1/second.ub,float("inf"))
        else:
            new_second = Interval(-float("inf"),float("inf"))
    return Interval_mul(first,new_second)

def Interval_min(first:Interval,second:Interval):
    values = [min(first.lb,second.lb), min(first.lb,second.ub), min(first.ub,second.lb), min(first.ub,second.ub)]
    return minimal_Interval(values)

def Interval_max(first:Interval,second:Interval):
    values = [max(first.lb,second.lb), max(first.lb,second.ub), max(first.ub,second.lb), max(first.ub,second.ub)]
    return minimal_Interval(values)

def Interval_sqr(interval:Interval):
    if 0 not in interval:
        values = [interval.lb*interval.lb, interval.ub*interval.ub]
    else:
        values = [0, interval.lb*interval.lb, interval.ub*interval.ub]
    return minimal_Interval(values)

def Interval_width(interval:Interval):
    return Interval.ub-interval.lb

def Interval_intersection(first:Interval,second:Interval):
    if first is empty_Interval or second is empty_Interval:
        return empty_Interval
    else:
        if first.ub<second.lb or second.ub<first.lb:
            return empty_Interval
        else:
            return Interval(max(first.lb,second.lb),min(first.ub,second.ub))

def Interval_union(first:Interval,second:Interval):
    if first is empty_Interval or second is empty_Interval:
        return empty_Interval
    else:
        if first.ub<second.lb or second.ub<first.lb:
            return empty_Interval
        else:
            return Interval(min(first.lb,second.lb),max(first.ub,second.ub))

def Interval_hull_union(first:Interval,second:Interval):
    if first is empty_Interval or second is empty_Interval:
        return empty_Interval
    else:
        return Interval(min(first.lb,second.lb),max(first.ub,second.ub))

# Definition:1 ends here
