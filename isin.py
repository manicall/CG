from PyQt5.QtCore import QPoint
def isIn_angle(p, t):
    i = ind = 0 # индекс точки
    n = len(p)
    q = p[-1]
    
    for i in range(n):
        if(code(t, q) == code(t, p[i])): pass # ничего не делать
        elif((code(t, p[i]) - code(t, q) + 3)%4 == 0): ind += 1
        elif((code(t, p[i]) - code(t, q) + 1)%4 == 0): ind -= 1
        elif(mul(diff(p[i], q), diff(t, q)) > 0): ind += 2
        else: ind -= 2
        q = p[i]
    
    return False if(ind==0) else True

def isIn_hLine(p, t): 
    result = False
    j = len(p) - 1
    for i in range(len(p)):
        if ((p[i].y() < t.y() and p[j].y() >= t.y() or p[j].y() < t.y() and p[i].y() >= t.y()) and
            (p[i].x() + (t.y() - p[i].y()) / (p[j].y() - p[i].y()) * (p[j].x() - p[i].x()) < t.x())):
                result = not result
        j = i
        
    return result

# код четверти
def code(t, q):
    if(q.x() - t.x() >= 0 and q.y() - t.y() >= 0): return 0   # первая четверть
    if(q.x() - t.x() < 0 and q.y() - t.y() >= 0):  return 1   # вторая четверть
    if(q.x() - t.x() < 0 and q.y() - t.y() < 0):   return 2   # третья четверть
    return 3;   # во всех остальных случаях

def diff(p1: QPoint, p2: QPoint):
    return QPoint(p1.x() - p2.x(), p1.y() - p2.y())

def mul(p1: QPoint, p2: QPoint):
    return p1.x() * p2.y() - p1.y() * p2.x()