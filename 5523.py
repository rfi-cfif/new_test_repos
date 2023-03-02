a = [[int(j) for j in i.split()] for i in open('5523.txt')]
k = 0
for s in a:
    pov = []
    nepov = []
    for x in s:
        if s.count(x) == 2:
            pov.append(x)
        elif s.count(x) == 1:
            nepov.append(x)
    if len(pov) > 0:
        flag = 1
        for i in pov:
            for j in nepov:
                if i <= j:
                    flag = 0
        if flag == 1:
            k += 1
print(k)
