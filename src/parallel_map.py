# Module providing the 'parmap' function for multiprocessing, which is used instead of
# multiprocessing.Pool.map.
# Code written by klaus se
# see http://stackoverflow.com/questions/3288595/multiprocessing-using-pool-map-on-a-function-defined-in-a-class

import multiprocessing


def fun(f, q_in, q_out):
    while True:
        i, x = q_in.get()
        if i is None:
            break
        print("process #", i)
        q_out.put((i, f(x)))


def parmap(f, X, processes=multiprocessing.cpu_count()):
    ''' Used instead of Pool.map function for parallel programming
    Input:
        f: callable, function to be called
        X: iterable. Apply f to each element in X, collecting the results in a list
            which is returned
        processes: optional, number of processes running at one time
    '''
    if processes is None:
        processes = multiprocessing.cpu_count()
    q_in = multiprocessing.Queue(1)
    q_out = multiprocessing.Queue()

    proc = [multiprocessing.Process(target=fun, args=(f, q_in, q_out))
            for _ in range(processes)]
    for p in proc:
        p.daemon = True
        p.start()

    sent = [q_in.put((i, x)) for i, x in enumerate(X)]
    [q_in.put((None, None)) for _ in range(processes)]
    res = [q_out.get() for _ in range(len(sent))]

    [p.join() for p in proc]

    return [x for i, x in sorted(res)]

if __name__ == '__main__':
    print(parmap(lambda i: 2 * i, [1, 2, 3, 4, 6, 7, 8]))