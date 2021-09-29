import random

if __name__ == '__main__':
    print("Exercise 1:")
    x = random.randrange(1000, 9999)
    lst = list(str(x))
    res = list(map(int, lst))
    res1, res2 = sum(res[:len(res)//2]), sum(res[-1:-len(res)//2 - 1:-1])
    if not len(res) % 2 and res1 == res2:
        print(x, "is lucky number!")
    else:
        print(x, "isn`t lucky number!")
    x = 5564
    lst = list(str(x))
    res = list(map(int, lst))
    res1, res2 = sum(res[:len(res)//2]), sum(res[-1:-len(res)//2 - 1:-1])
    if not len(res) % 2 and res1 == res2:
        print(x, "is lucky number!")
    else:
        print(x, "isn`t lucky number!")
    x = input("Input number: ")
    lst = list(x)
    res = list(map(int, lst))
    res1, res2 = sum(res[:len(res)//2]), sum(res[-1:-len(res)//2 - 1:-1])
    if not len(res) % 2 and res1 == res2:
        print(x, "is lucky number!")
    else:
        print(x, "isn`t lucky number!")


    print("\nExercise 2:")
    x = random.randrange(100000, 999999)
    lst = list(str(x))
    res = list(map(int, lst))
    if not len(res) % 2 and res[:len(res)//2] == res[-1:-len(res)//2 - 1:-1]:
        print(x, "is palindrome number!")
    else:
        print(x, "isn`t palindrome number!")
    x = 123321
    lst = list(str(x))
    res = list(map(int, lst))
    if not len(res) % 2 and res[:len(res)//2] == res[-1:-len(res)//2 - 1:-1]:
        print(x, "is palindrome number!")
    else:
        print(x, "isn`t palindrome number!")
    x = input("Input number: ")
    lst = list(x)
    res = list(map(int,lst))
    if not len(res) % 2 and res[:len(res)//2] == res[-1:-len(res)//2 - 1:-1]:
        print(x, "is palindrome number!")
    else:
        print(x, "isn`t palindrome number!")

    print("\nExercise 3:")
    RADIUS = 4
    a, b = 0, 0
    print("Circle:")
    print("Center coordinate: O(", a, ";", b, ")")
    print("Radius = ", RADIUS)
    x = int(input("X = "))
    y = int(input("Y = "))
    if (x - a)**2 + (y - b)**2 < RADIUS**2:
        print("This point lies inside the circle!")
    else:
        print("This point don`t lies inside the circle!")
    


