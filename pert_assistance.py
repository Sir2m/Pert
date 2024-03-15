import numpy as np
import pandas as pd
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

print(time([2, 10, 8, 10, 7, 9, 3, 5], [4, 12, 9, 15, 7.5, 9, 3.5, 5], [12, 26, 10, 20, 11, 9, 7, 5]))