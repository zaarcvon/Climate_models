import matplotlib.pyplot as plt
import numpy as np
L_points=[L for L in range(1350,1150,-10)]  ##list of the Sun  intensity values
T_list=[] ##temperature list
it_list=[] ##iteration counts list
albedo=0.15 #start albedo

for L in L_points: 
    for it in range(0,100,1):  
        T=((L*(1-albedo)/4)/5.67E-8)**0.25  #calculate temperature
        albedo=round((-0.01*T+2.8),3)       #calculate albedo

        if albedo>0.65:albedo=0.65          #albedo constrains
        elif albedo<0.15:albedo=0.15        #albedo constrains
     
        T_list.append(T)                    ##add values to list
        it_list.append(it)
    T_list.append(np.NAN)                   ##add np.NAN to list for better visualisation
    it_list.append(np.NAN)
#plotting function
plt.xlabel('iterations (10 W/m2 each)',fontsize=14)
plt.ylabel('T,°K',fontsize=14)
plt.plot(it_list,T_list)
plt.arrow(75,235,-15,-5,shape='full',head_width=1, head_length=2,color='red')   #nice arrow
plt.text(70,236,'L=1250 W/m2',fontdict={'color':'red','weight':'bold','fontsize':12})  #at what Sun intensity values glaciation begins
plt.show()