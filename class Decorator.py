import time

class Time_decorator:
    def __init__(self, some_func):
        self.func = some_func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        a = self.func(*args, **kwargs)
        end_time = time.time()
        delta_time = end_time - start_time
        print(f'{round(delta_time, 10)} ms')
        return a

@Time_decorator
def degree(x):
    for i in range(10):
        for k in range(i):
            y = x**1000
    return y

if __name__ == '__main__':
    aaa = degree(5)
    print(aaa)


