from PyQt5.QtCore import QPoint

def isin(t):
    # 0 - если точка t не принадлежит многоугольнику,
    # не 0 - в других случаях
    i = ind = 0 # индекс точки
    
    n = 5
    p = [QPoint() for i in range(n)] # !массив точек многоугольника
    
    q = p[-1]
    
    for i in range(n):
        if(code(t, q) == code(t, p[i])): pass # ничего не делать
        elif((code(t, p[i]) - code(t, q) + 3)%4 == 0): ind += 1
        elif((code(t, p[i]) - code(t, q) + 1)%4 == 0): ind -= 1
        elif((p[i] - q) * (t - q) > 0): ind += 2
        else: ind -= 2
        q = p[i]
        
    return False if(ind==0) else True

# код четверти
def code(t, q):
    if(q.x() - t.x() >= 0 and q.y() - t.y() >= 0): return 0    # первая четверть
    if(q.x() - t.x() < 0 and q.y() - t.y() >= 0): return 1     # вторая четверть
    if(q.x() - t.x() < 0 and q.y() - t.y() < 0): return 2      # третья четверть
    return 3;   # во всех остальных случаях
