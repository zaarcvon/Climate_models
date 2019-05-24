import matplotlib.pyplot as plt

timeStep = 20           # years
waterDepth = 4000        # meters
L = 1350                 # Watts/m2
albedo = 0.3
epsilon = 1
sigma = 5.67E-8   
T=0                   #start temperature
hc=4218                 #heat capacity for the water at 273°K and atmospheric pressure 0.1 bar (it's just a model)

nSteps = int(input(""))

times=[i for i in range(0,timeStep*nSteps,timeStep)]  #list of time steps
temps=[] # list of the temperatures for each time step, first temperature are from the var above
outcome=[]    # list of the heat outflux from the surface for each time step
for i in times:
    temps.append(T) 
    outcome.append(epsilon*sigma*(T**4))
    inp=L*(1-albedo)*timeStep*311.04E5/4  ##input heat from the Sun
    out=epsilon*sigma*(T**4)*timeStep*311.04E5  ##output heat from the surface
    T=(inp-out)/(waterDepth*1.0E3*hc)+T  ##resulted temperature of the body

#Next goes visualisiation of the results
fig,ax1 = plt.subplots()
plt.title('Temperature and heat flux from the surface')
                #First axis is a temperature curve
color = 'tab:red'
ax1.plot(times,temps,color=color)
ax1.set_ylabel('Temp, °K', color=color,rotation=45,fontsize=14,labelpad=20)
ax1.tick_params(axis='y', labelcolor=color)
                #Second axis is a heat flux curve
color = 'tab:blue'
ax2=ax1.twinx()
ax2.set_ylabel('Heat flux, W/m2', color=color,rotation=45, fontsize=14,labelpad=40)
ax2.plot(times,outcome)
ax2.tick_params(axis='y', labelcolor=color,)
ax1.set_xlabel('years',fontsize=14)
plt.show()