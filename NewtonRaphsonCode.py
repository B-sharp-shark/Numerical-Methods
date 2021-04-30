import math
# METHOD: NEWTON RAPHSON

H1 = 24831 #J/mol
H2 = -5118 #J/mol
m0 = 0.06156  #kg/kg
R = 8.314  #J/mol/K
T = (52.6 + 273.15) #k
C0 = 0.001645
K0 = 5.710
Xe = 0.133 #kg/kg
a = 0.5

##best answer 0.6480666248504123
C = C0*math.exp(H1/(R*T))
K = K0*math.exp(H2/(R*T))

def fnEval(a):
    # evaluates the function at a
    return math.pow(a,2)* math.pow(K,2)*Xe*(1-C) + a*K*(C*(Xe-m0)-(2*Xe)) + Xe

def diffEval(a):
    # evaluates the differential of the function at a
    return 2*a* math.pow(K,2)*Xe*(1-C) + K*(C*(Xe-m0)-(2*Xe))


print("Initial guess: ", a)
#print(fnEval(0.6480666248504123))
n= 20 # stopping criterion (number of iterations)
while(n>0):
    # using newton raphson formula
    
    a = a - (fnEval(a)/diffEval(a))
    print("At Iteration",20-n+1,", a=",a)
    n = n-1

input()
