class Person():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.created_on=dt.utcnow()
        print(self.full_name, "is Alive!!!!")

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        '''Human Readable Output -- should be unique'''
        return f'<Person | {self.full_name}>'

    def __repr__(self):
        '''Machine Readable unique Output'''
        return f'<Person | {self.last_name} {self.created_on.strftime("%c")}>'

    def __hash__(self):
        return hash(self.full_name+self.created_on.strftime("%c"))

    def __bool__(self):
        return self.age > 0

    def __del__(self):
        print(f"Our person {self.full_name} has died")

    def __eq__(self, __o):
        return self.age == __o.age
    
    # less than
    def __lt__(self, __o):
        return self.age < __o.age
    
    # Greater Than
    def __gt__(self, __o):
        return self.age > __o.age

    # Less than or Equal too
    def __le__(self, __o):
        return self.age <= __o.age

    # greater than or Equal too
    def __ge__(self, __o):
        return self.age >= __o.age

# steve = Person('Steve', 'Scuba', 33)
# print(steve.full_name)
# steve.first_name = "Joe"
# print(steve.full_name)
# print(steve)
# print(repr(steve))
# print(hash(steve))

matt = Person(first_name="Matt", last_name = "Leblanc", age = 53)
lisa = Person(first_name="Lisa", last_name = "Kudrow", age = 55)
steve = Person(first_name="Steve", last_name ="Nash", age = 55)
bambam = Person(first_name="BamBam", last_name="Rubble", age = 0)

# if matt:
#     print("Matt is alive")
# else:
#     print("Matt hasn't been born")

# if bambam:
#     print("BamBam is alive")
# else:
#     print("BamBam hasn't been born")

# print(bool(bambam))
print(bambam == steve)

print(lisa == steve) # True
print(steve > lisa) # False
print(steve < lisa) # False
print(steve >= lisa) # True
print(steve <= lisa) # True
print("="*20)

print(lisa == matt) # False
print(matt > lisa) # False
print(matt < lisa) # True
print(matt >= lisa) # False
print(matt <= lisa) # True

group = [lisa, bambam, steve, matt]
print(sorted(group, reverse=True))
for person in group:
    print(person)


# make a Class of Car that that will be sorted by its year