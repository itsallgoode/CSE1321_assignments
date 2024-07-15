class Dog:
    
    def __init__(self, age=0, weight=0.0, name='', furColor='', breed=''):
        self.age = age
        self.weight = weight
        self.name = name
        self.furColor = furColor
        self.breed = breed

    def bark(self):
        print("Woof! Woof!")

    def rename(self):
        new_name = input(f"{self.name} isn't a very good name. What should they be renamed to: ")
        self.name = new_name

    def eat(self):
        food = float(input(f"{self.name} is hungry, how much should he eat: "))
        self.weight += food
    
def main():

    d1 = Dog()
    
    print("You are about to create a dog.")
    d1.age = int(input("How old is the dog: "))
    d1.weight = float(input("How much does the dog weigh: "))
    d1.name = input("What is the dog's name: ")
    d1.furColor = input("What color is the dog: ")
    d1.breed = input("What breed is the dog: ")
    print(f"{d1.name} is a {d1.age} year old {d1.furColor} {d1.breed} that weighs {d1.weight} lbs.")
    d1.bark()
    d1.eat()
    d1.rename()
    print(f"{d1.name} is a {d1.age} year old {d1.furColor} {d1.breed} that weighs {d1.weight} lbs.")

main()