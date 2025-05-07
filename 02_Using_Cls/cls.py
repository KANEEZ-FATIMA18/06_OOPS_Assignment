class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_counter(cls):
        print(f"My total created objects are: {cls.count}")  


object1 = Counter()          
object2 = Counter()          
object3 = Counter()          
object4 = Counter()          
object5 = Counter()          
object6 = Counter()          
object7 = Counter()      

Counter.display_counter()  # Output: My total created objects are: 7