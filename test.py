# import matplotlib.pyplot as plt
timeStep = 100           # years
waterDepth = 4000        # meters
L = 1350                 # Watts/m2
albedo = 0.3
epsilon = 1
sigma = 5.67E-8   
c = 4170                  #Joul|kg*K
nSteps = int(input(""))
T=0
times=[i for i in range(0,timeStep*nSteps,timeStep)]
temps=[0]
for i in times:
    inp=L*(1-albedo)*timeStep*311.04E5/4
    out=epsilon*sigma*(T**4)*timeStep*311.04E5
    T=(inp-out)/(waterDepth*1.0E3*c)+T
    temps.append(T)
# plt.plot(times,temps)
# plt.scatter(times,temps)
out=epsilon*sigma*(temps[-1]**4)
print(temps[-1],out)