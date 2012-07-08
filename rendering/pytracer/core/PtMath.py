from math import *

def quadratic(A,B,C):
    # find quadratic discriminant
    discrim = B * B - 4. * A * C; 

    if discrim < 0.:
        return False,0.,0.
    
    rootDiscrim = sqrt(discrim);
    # Compute quadratic _t_ values
    if B < 0:
        q = -.5 * (B - rootDiscrim)
    else:
        q = -.5 * (B + rootDiscrim)

    t0 = q / A
    t1 = C / q
    if t0 > t1:
        tmp = t1
        t1 = t0
        t0 = tmp
    return True,t0,t1
