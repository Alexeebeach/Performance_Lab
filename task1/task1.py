import sys
from itertools import cycle 

if __name__ == '__main__':
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    if len(sys.argv) > 2:
        m = int(sys.argv[2])
    mas = list(range(1,n+1))
    path = 0
    tempMas = list(range(1,m+1))
    k = 0
    for i,j in enumerate(cycle(mas)):
    	if tempMas[m-1] == 1:
    		break
    	tempMas[k] = j
    	if k == m-1:
    		path = path*10 + tempMas[0]
    		k=0
    		tempMas[k] = j
    	k+=1
    	
    print(path)