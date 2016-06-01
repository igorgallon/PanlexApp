import time
import datetime
import math
from datetime import timedelta

def subDateFloat(date1, date2):
    aux1 = date1 - date2
    aux2 = aux1.total_seconds()/timedelta(days=1).total_seconds()
    aux2 = math.fabs(aux2)
    return aux2

def remainingTime(x):
    aux = subDataFloat(x.getDeadline(), datetime.datetime.now()) / subDataFloat(x.getDeadline(), x.getCreationDate())
    return aux

def notCompleted(x):
    aux = (x.getWorkload() - x.getDone()) / x.workload()
    return aux


