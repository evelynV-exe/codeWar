def get_size(w,h,d):
    sa = 2*(d*w + d*h + w*h)
    v = w*h*d
    return [sa, v]
