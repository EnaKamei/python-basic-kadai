def calculate_total(price,tax):
    total = price * ( 1 + tax/100 )
    return total

result = calculate_total(100,10)
print(f"{result}円")