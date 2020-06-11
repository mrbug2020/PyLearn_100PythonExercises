#! python3
"""
Câu hỏi: Định nghĩa một lớp gồm có tham số lớp và có cùng tham số instance
"""


class Person(object):
    name = "Person"

    def __init__(self, name):
        self.name = name


def ex():
    exercisePerson = Person("exercisePerson")
    print(f"{Person.name} name is {exercisePerson.name}")
    testPerson = Person("Test person")
    print(f"{Person.name} name is {testPerson.name}")


def main():
    ex()


def test():
    print("unit test success.")


if __name__ == "__main__":
    test()
    main()
