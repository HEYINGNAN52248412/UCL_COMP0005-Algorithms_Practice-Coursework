id = list(range(10))
size = [1]*10

def root (i):
    while id[i] != i:
        id[i] = id[id[i]]
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