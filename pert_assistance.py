import numpy as np
import pandas as pd
from scipy.stats import norm
import string

def time(op, ml, pem):
    n = len(op)
    alph = list(string.ascii_uppercase)
    op = np.array(op)
    pem = np.array(pem)
    ml = np.array(ml)
    
    if not (op.size == pem.size & pem.size == ml.size):
        print("error")
        return 0
    
    t = (op + pem + (4 * ml)) / 6
    v = ((pem - op) / 6) ** 2
    print('Given Data:\n', np.concatenate([op.reshape(1, n), ml.reshape(1, n), pem.reshape(1, n)]).transpose())
    data = {
        'Time': t,
        "Variance": v
    }
    t = pd.DataFrame(data, index=[alph[i] for i in range(n)])
    return t


def inp_loop(typ, n):
    x = 0
    l = []
    for _ in range(n):
        while True:
            try:
                x = float(input(f"Enter {typ} time {_ + 1}: "))
                l.append(x)
                break
            except KeyboardInterrupt:
                quit()
            except:
                pass
    print('end')
    return l


def critical_path(n):
    x = ''
    l = []
    for _ in range(n):
        x = input(f"Enter Letter {_ + 1}: ")
        l.append(x.upper())
    print('end')
    return l


n = int(input('Enter the data length: '))
print('okay')

op = inp_loop('optimistic', n)
ml = inp_loop('most likely', n)
pem = inp_loop('pessimistic', n)

t = time(op, ml, pem)
print(t)

nn = int(input('no of critical path points: '))
print('okay')

cp = critical_path(nn)

var = 0

for _ in range(nn):
    var += t['Variance'][cp[_]]

print(f"Variance = {var}")

et = int(input('Estimated time: '))
p = int(input('Probability at? '))

z = (p - et) / np.sqrt(var)
print(f'z = {z}')

print(norm.cdf(z))
