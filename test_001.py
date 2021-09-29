a = "2233344445555566622"
#O / P: 223344556322

count = 0
res_str = ''
for i,j in enumerate(a):
    if i > 0:
        if a[i] == a[i-1]:
            count = count + 1
            if i == (len(a) - 1):
                res_str = res_str + str(a[i - 1]) + str(count)
        else:
            res_str = res_str + str(a[i - 1]) + str(count)
            count = 1
    else:
        count = 1

print(res_str)
