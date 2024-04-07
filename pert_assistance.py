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
        print("Size Error, Problem in the code or input")
        return 0
    
    t = (op + pem + (4 * ml)) / 6
    v = ((pem - op) / 6) ** 2
    print('Given Data:\n', np.concatenate((op.reshape(n, 1), ml.reshape(n, 1), pem.reshape(n, 1)), axis=1))
    data = {
        'Time': t,
        "Variance": v
    }
    table = pd.DataFrame(data, index=[alph[i] for i in range(n)])
    return table


def inp_loop(typ, n):
    x = 0
    l = []
    for _ in range(n):
        while True:
            try:
                x = float(input(f"Enter {typ} time for activity {_ + 1}: "))
                l.append(x)
                break
            except KeyboardInterrupt:
                quit()
            except:
                pass
    print(f'{typ} end')
    return l


def critical_path(n):
    x = ''
    l = []
    for _ in range(n):
        x = input(f"Enter critical path node {_ + 1}: ")
        l.append(x.upper())
    print('end')
    return l


n = int(input('Number of activities: '))
print('okay')

op = inp_loop('optimistic', n)
ml = inp_loop('most likely', n)
pem = inp_loop('pessimistic', n)

table = time(op, ml, pem)
print(table)

nn = int(input('Number of critical path nodes: '))
print('Starting ...')

cp = critical_path(nn)
var = 0
et = 0

for _ in range(nn):
    var += table['Variance'][cp[_]]
    et += table['Time'][cp[_]]
print(f"Variance = {var}\nEstimated Time = {et}")

p = float(input('Probability at: '))

z = (p - et) / np.sqrt(var)
print(f'z = {z}')

print(norm.cdf(z))
