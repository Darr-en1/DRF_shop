a = sorted([-4, -5, -10, 3, 6, 10], key=lambda x: (x < 0, abs(x)))
print(a)
