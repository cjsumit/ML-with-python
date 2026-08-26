import numpy as np
m2=np.array([[1,2,3],[4,5,6],[7,8,9]])

sum=0
for i in np.nditer(m2):
    sum=sum+i
print(sum)
print()
mt2=m2.T

print(mt2)


