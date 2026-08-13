def square(side):
    area = side * side
    if area % 1 != 0:
        area = int(area) + 1
    return area


print(square(4))
print(square(4.2))
print(square(4.9))
