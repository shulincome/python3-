##熟悉类和继承之间的关系
## Animal is-a object(yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

# Dog is-an Animal 
class Dog(Animal):
    
    def __init__(self, name):
        #Dog has-a name to named.
        self.name = name

# Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        #Cat has-a name to named.
        self.name = name

##Person is-a object 
class Person(object):
    
    def __init__(self, name):
        #Person has-a name to named.
        self.name = name

        ##Person has-a pet of some kind.
        self.pet = None


#Employee is-a Person.
class Employee(Person):

    def __init__(self, name, salary):
        ##??hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ##Employe has-a salary to named.
        self.salary = salary

## Fish is-a object.
class Fish(object):
    pass

##Salmon is-a Fish.
class Salmon(Fish):
    pass

#Halibut is-a Fish.
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

##satan is-a Cat
satan = Cat("Satan")

##mary is-a Person.
mary = Person("Mary")

## mary has-a pet named satan
mary.pet = satan

## frank is-a Employee ,and has-a salary=120000
frank = Employee("Frank", 1200000)

##frank has-a pet named rover
frank.pet = rover

##??
flipper = Fish()

##??
crouse = Salmon()

##??
harry = Halibut()