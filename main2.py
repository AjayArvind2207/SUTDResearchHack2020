import numpy as np
def linear_connectivity(L, enter=[1]):
    C = np.zeros((L+2, L+2))
    for i in range(1, L+1):
        C[i][i+1] = 1
    for e in enter:
        C[0][e] = 1
    C[-1][-1] = 1
    return C
def add_junction(main, pos, branches):
    length = len(main)
    branch_lens = [len(branch) - 2 for branch in branches]
    length += sum(branch_lens)
    C = np.zeros((length, length))
    C[:len(main)-2, :len(main)] = main[:-2]
    print(C)
    C[len(main)-2][-1] = 1
    branch_start = len(main)-1
    for branch in branches:
        C[pos, branch_start] = 1
        C[branch_start:branch_start+len(branch)-3, branch_start+1:branch_start+len(branch)-1] += branch[1:-2, 2:]
        C[branch_start+len(branch)-3, -1] = 1
        branch_start += len(branch) - 2
    C[-1, -1] = 1
    return C
m = linear_connectivity(5)
b = linear_connectivity(2)
print(add_junction(m, 2, [b, b]))
H = np.zeros((10, 100))