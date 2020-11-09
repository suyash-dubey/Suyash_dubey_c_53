def summer_69(list):
    sum=0
    x=len(list)
    if(6 in list and 9 in list):
        a=list.index(6)
        b=list.index(9)
        if(a<b):
            del list[a:b+1]
            y=len(list)
            for i in range(y):
                sum=sum+list[i]
            print(sum)
        else:
            for i in range(x):
                sum=sum+list[i]
            print(sum)
    else:
        for i in range(x):
            sum=sum+list[i]
        print(sum)
list=[4,5,6,7,8,9]
summer_69(list)
