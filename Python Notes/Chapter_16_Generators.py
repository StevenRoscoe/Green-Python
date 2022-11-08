#A generator is a kind of function that returns an iterator, which is an objects that can be looped over like a list.
def gen_range(stop, start=1, step=1):
    num = start
    while num <= stop:
        yield num
        num += step
        
def gen_fib():              #infinite generator
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a