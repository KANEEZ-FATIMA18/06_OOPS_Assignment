class Dog:
    def __init__(self , name , breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof Woof!")  


dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Bulldog")
dog3 = Dog("Bella", "Labrador")


dog1.bark() 
dog2.bark()
dog3.bark()
