from math import factorial as fact

def soch_bez_povt (k,n):
    return fact(n) / (fact(k) * (fact(n-k)))

def soch_s_povt (k,n):
    return fact(k+n-1) / (fact(n-1) * fact(k))


var_conter = 4
degree = 4
counter = 0
for k in range(1,degree+1):
    counter += soch_s_povt(k, var_conter)
print(counter)

comb = 0
for k in range(1,int(counter)+1):
    comb += soch_bez_povt(k,counter)
print(comb)