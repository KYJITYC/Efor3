def VseProstie(r=0):
    if r == 0:
        r = int(input('interval:')) + 1
    else:
        r += 1
    a = [True] * r
    pr = []
    a[0] = a[1] = False
    for k in range(2, r):
        if a[k] is True:
            for m in range(2 * k, r, k):
                a[m] = False
    for k in range(r):
        if a[k] is True:
            pr.append(k)

    return (pr)


def SummaProstih(r=0):
    if r == 0:
        r = int(input('interval:')) + 1
    else:
        r += 1
    return (sum(VseProstie(r)))



