id = list(range(10))
size = [1]*10

def root (i):
    while id[i] != i:
        i = id[i]
    return i

def find (u,v):
    u_root = root(u)
    v_root = root(v)

    return u_root == v_root

def union (u,v):
    u_root = root(u)
    v_root = root(v)

    if size[u_root]>size[v_root]:
        id[v_root] = u_root
    else:
        id[v_root] = u_root


'''
Only when the tree containing X (the smaller tree) is merged beneath another larger or equal tree (the larger tree) does X's depth increase by one.
when this happened, the size of the tree that containing X will at least get DOUBLED 
if the depth of X is 1 at the beginning:
depth+1 -> size+2
depth+2 -> size+4
......
depth+n -> size+2^n

we know that we have N nodes, so the MAX depth k = log↓2(N)
'''