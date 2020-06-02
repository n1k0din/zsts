def powers(to_pow):
    for power in range(to_pow + 1):
        yield lambda x: pow(x, power)


print([p(2) for p in powers(16)])




