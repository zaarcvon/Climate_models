import numpy
nYears = float( input('') )
nX = 10                # number of grid points
domainWidth = 1e6      # meters
timeStep = 1         # years
flowParam = 1e4        # m horizontal / yr
snowFall = 0.5         # m / y
elevation = numpy.zeros(nX+2)
flow = numpy.zeros(nX+1)
dX = domainWidth / nX

for time in numpy.arange(0,nYears,timeStep):
    for ix in range(0,len(flow)):
        flow[ix] = ( elevation[ix] - elevation[ix+1] ) / dX * flowParam * ( elevation[ix]+elevation[ix+1] ) / 2 / dX
    for ix in range(1,len(elevation)-1):
        elevation[ix]+=(snowFall + flow[ix-1] - flow[ix])*timeStep
print(elevation[5])