L, albedo, nIters = input("").split()
L, albedo, nIters = [ float(L), float(albedo), int(nIters) ]  
for it in range(0,nIters):
    T=((L*(1-albedo)/4)/5.67E-8)**0.25
    albedo=-0.01*T+2.8
    if albedo>0.65:albedo=0.65
    elif albedo<0.15:albedo=0.15
print(round(T,3),round(albedo,3))