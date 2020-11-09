def spy_game(list):
    x=len(list)
    for i in range(0,x):
        if(list[i]==0):
              for i1 in range(i+1,x):
                    if(list[i1]==0):
                        for i2 in range(i1+1,x):
                            if(list[i2]==7):
                                return True
                    else:
                        return False
list=[1,2,0,0,4,5,7]
spy_game(list)