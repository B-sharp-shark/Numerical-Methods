import math
# METHOD: BI-SECTION

H1 = 24831 #J/mol
H2 = -5118 #J/mol
m0 = 0.06156  #kg/kg
R = 8.314  #J/mol/K
T = (52.6 + 273.15) #k
C0 = 0.001645
K0 = 5.710
Xe = 0.133 #kg/kg
a = 0
b = 1
m = 0
a = 0.6480666248504123


C = C0*math.exp(H1/(R*T))
K = K0*math.exp(H2/(R*T))

s =math.pow(a,2)* math.pow(K,2)*Xe*(1-C) + a*K*(C*(Xe-m0)-(2*Xe)) + Xe
y = ((C*K*a*m0)/(1-(a*K))*(1-(K*a)+(C*K*a))) -Xe
print(s)
print(y)

def fnEval(a):
    # Evaluate function of a, written as quadratic equation
    return math.pow(a,2)* math.pow(K,2)*Xe*(1-C) + a*K*(C*(Xe-m0)-(2*Xe)) + Xe

#print(fnEval(0.6480666248504123))
print("initial values: a=0, b=1")

n= 70 # Stopping criterion (number of itertions)
while(n>0):
    m = (a + b)/2 # find mid point
    if fnEval(a) * fnEval(m) < 0:
        b = m # if a solution exits set m as b
        print("At Iteration",70-n+1,", a=",m)
    elif fnEval(b) * fnEval(m) < 0:
        a = m # if a solution exits set m as a
        print("At Iteration",70-n+1,", a=",m)
    else: # if function at m evaluates to zero, the exact root has been found
        print("Root of the functiion: ", m)
        break
    n = n-1

input()
