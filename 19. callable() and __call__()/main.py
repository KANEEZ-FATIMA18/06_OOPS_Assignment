class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

m = Multiplier(5)
print(callable(m))  
print(m(10))        
