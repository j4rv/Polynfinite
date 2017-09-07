# Polynfinite
A python script that creates wallpapers using a base polygon


## A huge oversampling with lots of iterations and a line width of '1' creates really smooth renders  
![First example](https://raw.githubusercontent.com/J4RV/Polynfinite/master/examples/Example%20One.png)  
Size: 1920x1080.  
Background color: (0, 0, 0)  
Oversampling: 10  
Polygon used: [(-4005, -504), (-7505, 4612), (36468, -3867), (8344, 20502), (21456, 14881)]  
Line width: 1.  
Ratio: 0.01.  
Iterations: 1000.  
(Colors: red=0, green="CENTER", blue=255)  

## Combining some colors!
![Second example](https://raw.githubusercontent.com/J4RV/Polynfinite/master/examples/Example%20Two.png)  
Size: 1920x1080.  
Background color: (0, 0, 0)  
Oversampling: 2  
Polygon used: [(-2028, 3629), (3317, 3666), (5134, 4074), (6086, 2574), (1142, -761)]  
Line width: 2.  
Ratio: 0.01.  
Iterations: 100.  
(Colors: red="CENTER", green="EXTERIOR", blue=255)  

## No oversampling, a low number of iterations and a line width of '1' creates pixelated renders  
![Third example](https://raw.githubusercontent.com/J4RV/Polynfinite/master/examples/Example%20Three.png)  
Size: 640x480.  
Background color: (0, 0, 0)  
Oversampling: 1  
Polygon used: [(-594, 80), (463, 682), (-599, 833), (1151, 96), (575, -366), (914, 910)]  
Line width: 1.  
Ratio: 0.05.  
Iterations: 64.  
(Colors: red=255, green=255, blue=255)  

