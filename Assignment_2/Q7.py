import math
def angle(x,y):
    return math.atan2(y,x)
def antipodal(points):
    n=len(points)
    if n<2:
        return False
    points.sort(key=lambda point:angle(point[0],point[1]))
    for i in range(n):
        x1,y1=points[i]
        x2,y2=points[(i+n//2)%n]
        if x1==-x2 and y1==-y2:
            return True
    return False

n=6
points=[(math.cos(2*math.pi*i/n),math.sin(2*math.pi*i/n)) for i in range(n)]
print(f"Points:{points}")
result=antipodal(points)
print(f"Are there antipodal points ?{result}")