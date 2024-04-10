class MyNumber:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return self.value + other.value
    
    def __sub__(self, other):
        return self.value - other.value
    
    def __mul__(self, other):
        return self.value * other.value
    
    def __truediv__(self, other):
        if other.value == 0:
            raise ZeroDivisionError("Dzielenie przez zero!")
        return self.value / other.value
    
    def __mod__(self, other):
        if other.value == 0:
            raise ZeroDivisionError("Dzielenie przez zero!")
        return self.value % other.value
    
    def __pow__(self, other):
        return self.value ** other.value
    
    def __xor__(self, other):
        return self.value ** other.value

    def __repr__(self):
        return str(self.value)
    
    def __call__(self, other):
        return self.value * other.value

# Przykładowe użycie
x = MyNumber(5)
y = MyNumber(2)

print("x + y =", x + y)
print("x - y =", x - y)
print("x * y =", x * y)
print("x / y =", x / y)
print("x % y =", x % y)
print("x ^ y =", x ^ y)