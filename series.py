
def series(n: int, var_suite: str, nb_rpt: int):
    print(f'u0 =', n, f'({var_suite})')
    for i in range(nb_rpt):
        print(f'u{i+1} =', int(eval(var_suite)))
        n = int(eval(var_suite))

series(10, '100 + n * 10', 25)
