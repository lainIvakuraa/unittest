def simple_condition(number: int) -> bool:
    if number > 10:
        return True
    else:
        return False
    
def more_conditions(first: int, second:int) -> bool:
    if first > 10 or second > 10:
        return True
    else:
        return False
print(more_conditions(5,5))

def moar_conditions(first: int, second:int) -> bool:
    if first >10:
        if second > 10 and first > 100:
            return True
        else:
            return False
    else: return False

def fizzbuzz_condition(number: int) -> str:
    if number % 3 == 0 and number % 5 == 0:
        return "fizzbuzz"
    if number % 3 == 0:
        return "fizz"
    if number % 5 ==0:
        return "buzz"
    return str(number)
def fast_sqrt(y:float) -> float:
    if y < 0:
        raise ValueError
    tolerance = 0.5
    prev = -1.0
    x = 1.0
    while abs(x-prev) > tolerance:
        prev =x
        x = x- (x*x -y) / (2 *x)
    return x