from multiprocessing import Process

def f(name):
    print('hello', name)


p = Process(target=f, args=('bob','tent'))
p.start()
p.join()
p.close()
