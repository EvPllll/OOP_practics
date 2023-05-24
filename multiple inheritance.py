class Goods:
    def __init__(self, name, weight, price):
        super().__init__()
        self.name = name
        self.weight = weight
        self.price = price

    def show_info(self):
        print(f'{"-" * 10}\nName: {self.name}\nWeight: {self.weight}\nPrice: {self.price}\n{"-" * 10}')


class MixingLog:
    ID = 0
    def __init__(self):
        self.ID += 1
        self.id = self.ID

    def show_log(self):
        print(f'{self.id}: saled')

class Notebook(Goods, MixingLog):
    pass

if __name__ == '__main__':
    notebook = Notebook('Dell Latitude 3410', 1.5, 40000)
    notebook.show_info()
    notebook.show_log()
    second_notebook = Notebook('some_Asus', 2.0, 45000)
    second_notebook.show_info()
    second_notebook.show_log()
