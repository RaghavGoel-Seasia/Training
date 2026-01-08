class Jar:
    def __init__(self, capacity):
        self.capacity = capacity
        self._number = 0
    
    @property
    def number(self):
        return self._number

    @property
    def capacity(self):
        return self._capacity
    
    @number.setter
    def number(self,number):
        if number > self._capacity:
            raise ValueError("Not enough room in the jar!")
        elif number < 0:
            raise ValueError("Not enough cookies in the jar!")
        else:
            self._number = number

    @capacity.setter
    def capacity(self,capacity):
        if capacity >= 0 and type(capacity) is int:
            self._capacity = capacity
        else:
            raise ValueError("Invalid capacity!!")
    
        
    def deposit(self, number):
        self.number += number 
    
    def withdraw(self,number):
        self.number -= number
     
        
    def __str__(self):
        return "🍪" * self.number
     