class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, *args, **kwargs):
        self.__counter += 1

    def show(self):
        print(self.__counter)

    def get(self):
        return self.__counter


if __name__ == '__main__':
    counter = Counter()
    counter()
    counter()
    counter()
    a = counter.get()
    print(a)


