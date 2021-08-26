import time
def lots_of_numbers(max):
    t1 = time.time()
    for x in range(0, max):
        print(x)
        time.sleep(.5)
    t2 = time.time()
    print('it took %s seconds' %(t2-t1))
    print("it took " + str(t2-t1)+" seconds" )
    

lots_of_numbers(30)