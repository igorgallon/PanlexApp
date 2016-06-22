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
    aux = subDateFloat(x.get_deadline(), datetime.datetime.now()) / subDateFloat(x.get_deadline(), x.get_creationDate())
    return aux

def notCompleted(x):
    aux = (x.get_workload() - x.get_done()) / x.get_workload()
    return aux