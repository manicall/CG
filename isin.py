from PyQt5.QtCore import QPoint
def isIn_angle(p, t):
    i = ind = 0 # индекс точки
    n = len(p)
    q = p[-1]
    
    for i in range(n):
        if(code(t, q) == code(t, p[i])): pass # ничего не делать
        elif((code(t, p[i]) - code(t, q) + 3)%4 == 0): ind += 1
        elif((code(t, p[i]) - code(t, q) + 1)%4 == 0): ind -= 1
        elif((p[i] - q) * (t - q) > 0): ind += 2
        else: ind -= 2
        q = p[i]
    
    return False if(ind==0) else True

def isIn_hLine(p, t):
    n = len(p)
    j = n-1
    
    for i in range(n):
        if (
            (((p[i].y <= t.y) and (t.y < p[j].y)) or 
             ((p[j].y<=t.y) and (t.y < p[i].y))) and
            (
                t.x < (p[j].x - p[i].x)*(t.y - p[i].y) / 
             (p[j].y - p[i].y) + p[i].x)):
        
            parity=1-parity
        
        j = (i := i + 1)
    
    return parity
    
# код четверти
def code(t, q):
    if(q.x() - t.x() >= 0 and q.y() - t.y() >= 0): return 0   # первая четверть
    if(q.x() - t.x() < 0 and q.y() - t.y() >= 0):  return 1   # вторая четверть
    if(q.x() - t.x() < 0 and q.y() - t.y() < 0):   return 2   # третья четверть
    return 3;   # во всех остальных случаях
