def maxRotateFunction(self, A):
    f = r = sum(i*x for i,x in enumerate(A)); s = sum(A)
    for x in reversed(A): f += s - len(A)*x; r = max(r,f)
    return r
