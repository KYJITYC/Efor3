
a = 1
n=0
sled = 1

while n<500:
    sled += 1  # sledujuschee chislo kotoroe nujno pribavit k summe prediduschih(a)
    a += sled
    n = 2

    for x in range(2,int(a**0.5//1+1)):
        if a % x == 0:
            n+=2# t k x do kornja iz a i vsegda 2 delitelja krome == kornju iz a
            if float(x)==a**0.5:
                n-=1

print(a,n)
