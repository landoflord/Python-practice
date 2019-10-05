import numpy as np
import scipy.stats as sps

def sec_av(A):
    s = np.array(A)
    for k in range(1, len(A)+1):
        s[k-1]= sum(np.delete(A,np.s_[k::]))/k
    return s

def stupid_sec_av(e):
    S = [0 for i in range(len(e))]
    for i in range(len(e)):
        for j in range(i+1):
            S[i] += round(e[j]/(i+1),8)
    return S
A = sps.uniform.rvs(size=10) 
S1 = sec_av(A)
S2 = stupid_sec_av(A)
print(S1)
print(S2)
print(np.abs(S1 - S2).sum())