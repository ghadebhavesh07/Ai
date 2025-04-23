import random

def hill_climb():
    x = random.uniform(-10, 10)
    step = 0.1

    def f(x): return -x**2 + 4

    while True:
        next_x = x + random.choice([-step, step])
        if f(next_x) > f(x):
            x = next_x
        else:
            break

    print("Best x:", round(x, 2), "Value:", round(f(x), 2))

hill_climb()