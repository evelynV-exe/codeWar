def polygon_area(a, b, c, d):
    sqrArea = a*b
    triangle = 0.5*(c - a)*b
    tol = sqrArea + triangle
    
    return tol
