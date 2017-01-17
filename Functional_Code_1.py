def get_primes(count):
"""
    The code returns the first counted integers
"""
result = []
x=2
while len(result) in range(count):
    i=2
    flag_n=0
    for i in range(2,x):
        if x%i == 0:
            flag_n+=1
            break
        i=i+1
    if flag_n == 0:
        result.append(x)
    x+=1
pass
return result
