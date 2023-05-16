from string import ascii_letters
class Person:
    RUS_LETTERS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя-'
    RUS_UPPER_LETTERS = RUS_LETTERS.upper()
    def __init__(self, full_name: str, age: int, passport_data: str, weight: float):
        self.full_name = full_name
        self.age = age
        self.passport_data = passport_data
        self.weight = weight

    @classmethod
    def verify_full_name(cls, full_name):
        if type(full_name) != str:
            raise TypeError('ФИО должны быть строкой.')

        full_name = full_name.split()
        if len(full_name) != 3:
            raise ValueError('Неверный формат ФИО.')

        letters = ascii_letters + cls.RUS_LETTERS + cls.RUS_UPPER_LETTERS

        for name in full_name:
            if len(name) < 1:
                raise ValueError('В ФИО должен быть хотя бы один символ.')
            if len(name.strip(letters)) != 0:
                raise ValueError('ФИО должны быть латинскими либо русскими символами.')

    @classmethod
    def verify_age(self, age):
        if type(age) != int or age < 0 or age > 120:
            raise TypeError('Возраст должен быть числом от 0 до 120.')

    @classmethod
    def verify_passport(cls, passport):
        if type(passport) != str:
            raise TypeError('Паспортные данные должны быть строкой.')

        passport_data = passport.split()
        if len(passport_data) != 2:
            raise ValueError('Неверный формат паспортных данных.')

        for data in passport_data:
            if not data.isdigit():
                raise ValueError('Паспортные данные должны быть числами')

        if len(passport_data[0]) != 4 or len(passport_data[1]) != 6:
            raise ValueError('Паспортные данные должны быть введены в формате "хххх хххххх')

    @classmethod
    def verify_weight(cls, weight):
        if type(weight) != float:
            raise TypeError('Вес должен быть числом с плавающей точкой.')
        if weight < 20:
            raise ValueError('Вес должен быть больше 20.')

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, full_name):
        self.verify_full_name(full_name)
        self.__full_name = full_name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.verify_age(age)
        self.__age = age

    @property
    def passport_data(self):
        return self.__passport_data

    @passport_data.setter
    def passport_data(self, passport_data):
        self.verify_passport(passport_data)
        self.__passport_data = passport_data

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight




if __name__ == '__main__':
    my_person = Person('Плюснин Евгений Владимирович', 27, '5231 143215', 79.2)
    my_person.age = 78
    full_name = my_person.full_name
    print(type(full_name))

    print(my_person.__dict__)

