def median(vals):
    vals.sort()
    z = len(vals)
    index = z / 2
    if z % 2 == 0:
       return mean([vals[index], vals[index - 1]])
