a, b, c, d, e, f = map(int, input().split())

print((c * e - b * f) // (a * e - b * d), end = ' ')
print((c * d - a * f) // (b * d - a * e))
