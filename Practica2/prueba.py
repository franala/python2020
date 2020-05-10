def A():
    def B():
        nonlocal x
        x = x + 1
        print (x)
    x = 2
    B()

A()
