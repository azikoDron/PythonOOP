# Замыкания && метод __call__

def adder(val):
    def inner(a):
        return val + a
    return inner


a = adder(5)

print(a)

print(a(3))
