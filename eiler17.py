def eiler17(n):
    n_list = []
    for i in str(n):  # разбиваем n по цифрам
        n_list.append(int(i))


    if len(n_list) <= 1:
        return len_1(n)
    elif len(n_list) == 2:
        return len_2(n_list)
    elif len(n_list) == 3:
        return len_3(n_list)
    elif int(n)==1000:
        return 11
    else:
        print('слишком длинное')


def len_1(n,add=0):
    n1 =     (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    len_n1 = (4, 3, 3, 5, 4, 4, 3, 5, 5, 4)
    for i in n1:
        if i == int(n):
            return len_n1[i]+add

def len_2(n_list,add=0):

    n2_x0 =     (1, 2, 3, 4, 5, 6, 7, 8, 9)
    len_n2_x0 = (3, 6, 6, 5, 5, 5, 7, 6, 6)

    n2_1x =     (1, 2, 3, 4, 5, 6, 7, 8, 9)
    len_n2_1x = (6, 6, 8, 8, 7, 7, 9, 8, 8)

    n2_xx =     (1, 2, 3, 4, 5, 6, 7, 8, 9)
    len_n2_xx = (3, 3, 5, 4, 4, 3, 5, 5, 4)

    if n_list[0]==0: # если в начале 0-на функция длины 1
        return (len_1(n_list[1],add))


    else:
        if n_list[1]==0:# если второе число 0 - то длина 10 20 30 и тд до 90
            for i in n2_x0:
                if i==n_list[0]:
                    return (len_n2_x0[i-1]+add)

        elif n_list[0]==1: # если второе число 1 - от 11 до 19
            for i in n2_1x:
                if i==n_list[1]:
                    return (len_n2_1x[i-1]+add)

        else: # от 21 до 99
            for i in n2_xx:
                if i == n_list[1]:
                    rez=len_n2_xx[i-1]

            for i in n2_xx:
                if i == n_list[0]:
                    rez = rez + len_n2_x0[i-1]  #+ '-' (twenty-one)
                    return (rez+add)

def len_3(n_list,add=0):

    n3_x00 =     (1, 2, 3, 4, 5, 6, 7, 8, 9)
    len_n3_x00 = (13, 13, 15, 14, 14, 13, 15, 15, 14)

    if n_list[0] == 0:  # если в начале 0-на функция длины 2
        del n_list[0]
        return len_2(n_list)
    if n_list[1] == 0 and n_list[2] == 0 :
        for i in n3_x00:
            if i == n_list[0]:
                add +=len_n3_x00[i - 1] -3 # сто, двести,...девятьсот
                return add

    for i in n3_x00:
        if i == n_list[0]:
            add += len_n3_x00[i - 1]  # сто и, двести и,...девятьсот и

    del n_list[0]

    return len_2(n_list,add)

Rez=0
for i in range(1,1001):
    print(i,eiler17(i))
    Rez+=eiler17(i)
print(Rez)













