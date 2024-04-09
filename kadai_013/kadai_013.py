def calculate_total(price,tax):
    total = price * ( 1 + tax/100 )

    print(f"{total}円")

calculate_total(100,10)