from sympy import symbols, diff
from sympy.solvers import solve
from sympy.plotting import *
from sympy import *

x,y = symbols('x y')

def critical_point(fn, xdm=[-15,15], ydm=[-15,15], showp=False, **kwargs) :
    pary = diff(fn, y)
    parx = diff(fn, x)
    paryy = diff(fn, y, 2)
    parxx = diff(fn, x, 2)
    parxy = diff(fn, x, y)
    cy = solve(pary, y)
    cx = solve(parx, x)
    D = parxx*paryy-(parxy)**2
    cp = []

    for i in cx:
        if (xdm[0]<= i <= xdm[1]):
            for n in cy:
                if (ydm[0]<= n <= ydm[1]):
                    if ((D.subs({x:i, y:n}))>0 and parxx.subs({x:i,y:n})>0):
                        cp.append([[i,n], 'Local Minimum'])
                    if ((D.subs({x:i, y:n}))>0 and parxx.subs({x:i,y:n})<0):
                        cp.append([[i,n], 'Local Maximum'])
                    if ((D.subs({x:i, y:n}))<0):
                        cp.append([[i,n], 'Saddle Point'])
                    if ((D.subs({x:i, y:n}))==0):
                        cp.append([[i,n], 'Additional work needs to be performed to classify this critical point'])
                

    print('The critical points for %s over the region : %s <= x <= %s , %s <= y <= %s are ...' %(str(fn),str(xdm[0]),str(xdm[1]),str(ydm[0]),str(ydm[1])))
        
    for i in cp:
        print(i[0], end=' ')
        print(i[1])
    

    if (showp==True):
        print('The partial derivative, Fx = ',parx)
        print('The partial derivative, Fy = ',pary)
        print('The partial derivative, Fxx = ',parxx)
        print('The partial derivative, Fyy = ',paryy)
        print('The partial derivative, Fxy = ',parxy)

    #plot3d(fn,(x,xdm[0],xdm[1]),(y,ydm[0],ydm[1]), title = 'Critical Points', show=True, xlabel='x', ylabel='y')
    return parx

critical_point(x**4-2*x**2+y**2-6*y+5, ydm = [-5,5], xdm = [-5,5])
