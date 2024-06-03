def recursive_func(n: int) -> str:
    if n < 1:
        print('n is less than 1')
    else:
        recursive_func(n - 1)
        print(n)
    
recursive_func(4)