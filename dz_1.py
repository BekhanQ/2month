class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        return (f"Person - {self.name}, birth_date - {self.birth_date}, "
              f"occupation - {self.occupation}, higher_education - {self.higher_education}")

bekhan_qubanov = Person("Bekhan", "31_03", "student", False)
print(bekhan_qubanov.introduce())

ali_qubanov = Person("Ali", "16_04", "student", False)
print(ali_qubanov.introduce())

john_wick = Person("John", "19_05", "driver", True)
print(john_wick.introduce())

