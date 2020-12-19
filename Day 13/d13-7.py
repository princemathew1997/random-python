#memory size of list and tuple
from sys import getsizeof
L = (x**2 for x in range(100000))
K =[x**2 for x in range(100000)]
print("L",getsizeof(L))
print("K",getsizeof(K))