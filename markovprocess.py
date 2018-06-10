# -*- coding: utf-8 -*-
"""

@author: wangz
"""
import numpy as np
import random
P = np.array([[0.8, 0.2], [0.7, 0.3]])


pi = np.array([0.43,0.57])
cv=1

while cv>0.0000000001:
    pi2=np.dot(pi,P);
    cv=abs(np.min(pi2-pi))
    pi=pi2;

print(pi)

def sampling(dist):
    d = dist.copy()
    l = len(d)
    for i in range(l):
        if i > 0:
            d[i] += d[i-1]
    u = random.random() * d[-1]
    for i in range(l):
        if d[i] >= u:
            break
    return i

test = [0]*10000

test[0] = random.randint(0,2)
for i in range(len(test)-1):
    if test[i] == 0:
        test[i+1] = sampling(P[0])
    else:
        test[i+1] = sampling(P[1])
    
#print(test)

count = np.array([[0]*2]*2)


for i in range(len(test)-1):
    if test[i] == 0:
        if test[i+1] == 0:
            count[0][0] += 1
        else:
            count[0][1] += 1
    if test[i] == 1:
        if test[i+1] == 0:
            count[1][0] += 1
        else:
            count[1][1] += 1

#print(count)

p1 = count[0][0]/sum(count)[0]
p2 = count[0][1]/sum(count)[0]
p3 = count[1][0]/sum(count)[1]
p4 = count[1][1]/sum(count)[1]       
print(p1,p2,p3,p4)

P0 = sum(count)[0]/(sum(count)[0]+sum(count)[1])
P1 = sum(count)[1]/(sum(count)[0]+sum(count)[1])
print(P0,P1)



