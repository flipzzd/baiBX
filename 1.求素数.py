def su(a,b):
    for i in range(a,b):
        for j in range(2,i):
            if i%j==0:
                print(f"{i}不是素数")
                break
            else:
                print(f"{i}是素数")
                break
su(100,200)
