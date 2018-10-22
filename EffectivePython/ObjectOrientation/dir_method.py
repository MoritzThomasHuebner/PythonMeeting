# Old Style class in python 2
class OldStylePerson:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def fullname(self):
        return "%s %s" % (self.name, self.surname)


# New Style class in python 2
class NewStylePerson(object):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def fullname(self):
        return "%s %s" % (self.name, self.surname)


jane = OldStylePerson("Jane", "Smith")
john = NewStylePerson("John", "Smith")

print(dir(jane))
print(dir(john))
