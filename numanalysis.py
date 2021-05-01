# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# written by JEEMIN KIM
# 2021년 5월 2일  02:03

# %%
import math
from mymods.vector import Vector

TSTEP = 0.0001
ICONS = [(20, 3.734, 0.752),(20, 3.681, 0.771),(40.3, 4.030, 1.218),(40.3, 3.969, 1.226),(60, 3.735, 1.062),(60, 3.790, 1.066)]
R=0.0254/2
MASS=0.000645
K = 1.2*0.47*math.pi*R**2/2
AG = Vector(0,-9.8)

SIGMA = 0.001
MSTEP = 0.000002


class Ball:
    def __init__(self, m, x, v):
        self.m = m
        self.x = x
        self.v = v
    def move(self, f):
        a = f*(1/self.m)
        self.x = self.x + self.v*TSTEP
        self.v = self.v + a*TSTEP
    def getdrag(self, k):
        arg = self.v.argument(radians=True)
        return -k*self.v.norm()**2*Vector(math.cos(arg),math.sin(arg))

def forward(o):
    force = o.m*AG+o.getdrag(K)
    o.move(force)

loopstr = ''
def isloop():
    global loopstr
    if loopstr == '+-+' or loopstr == '-+-':
        print('looping!!')
    elif len(loopstr) > 3:
        loopstr = ''




# %%
d = 0
masses = []
obj = Ball(MASS,Vector(),Vector())
for con in ICONS:
    angle, v0, l = con
    rangle = math.radians(angle)
    while True:
        obj.x = Vector(0,0)
        obj.v = Vector(v0*math.cos(rangle),v0*math.sin(rangle))
        while obj.x[1]>=0:
            forward(obj)
        d = obj.x[0]
        if d-l > SIGMA:
            obj.m = obj.m - MSTEP
            loopstr += '-'
            isloop()
        elif d-l<-SIGMA:
            obj.m = obj.m + MSTEP
            loopstr += '+'
            isloop()
        else:
            masses.append(obj.m)
            print(masses)
            obj.m = MASS
            break


