class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        print(f'Меня зовут {self.name}. Я родился(ась) {self.birth_date}. Я работаю {self.occupation}. ')


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, classroom):
        super().__init__(name, birth_date, occupation, higher_education)
        self.classroom = classroom

    def introduce(self):
        print(f'Меня зовут {self.name}. Я родился(ась) {self.birth_date}. Я работаю {self.occupation}. '
              f'Класс {self.classroom}')


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby
    def introduce(self):
        print(f'Меня зовут {self.name}. Я родился(ась) {self.birth_date}. Я работаю {self.occupation}. '
              f'Хобби {self.hobby}')



classmate1 = Classmate(name="Бека", birth_date="5.12.2009", occupation="Программист", higher_education=False, classroom=123)
classmate1.introduce()
classmate2 = Classmate(name="Тима", birth_date="31.03.2010", occupation="Футболист", higher_education=False, classroom=123)
classmate2.introduce()
friend1 = Friend(name='Али', birth_date='16.04.2009', occupation='Продюссер', higher_education=False, hobby='баскетбол')
friend1.introduce()
friend2 = Friend(name='Алихан', birth_date='05.05.2010', occupation='Футболист', higher_education=False, hobby='Футбол')
friend2.introduce()
