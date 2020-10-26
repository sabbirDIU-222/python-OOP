# exception handling
try:
    x = 0
    num = 10
    res = num/x
    print(res)
except (ZeroDivisionError,Exception) as a:
    print(a)


finally:
    print("love y")

# what if we rise an error

def age(age):
    if age<18:
        raise ValueError("put valied nmumber ")
    return "you are allowed to vote"
try:
    print(age(17))
except ValueError as a:
    print(a)

finally:
    print("yoyo")


