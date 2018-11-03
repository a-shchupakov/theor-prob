from fractions import Fraction as fr


def build_table(random_variable):
    result = ''
    for k, v in sorted(random_variable.items()):
        result += '{} -> {}\r\n'.format(str(int(k)), str(v))
    return result


def get_const_rv(value):
    return {value: 1}


def transform_random_variable(rv_1, rv_2, transform):
    new_rv = {}
    for k1, v1 in rv_1.items():
        for k2, v2 in rv_2.items():
            key, value = transform(k1, k2), v1 * v2
            if key not in new_rv:
                new_rv[key] = 0
            new_rv[key] += value

    return new_rv


def gcd(a, b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)


def main():
    rv_1 = {1: fr(1, 6), 2: fr(1, 6), 3: fr(1, 6), 4: fr(1, 6), 5: fr(1, 6), 6: fr(1, 6)}
    rv_2 = {1: fr(1, 12), 2: fr(1, 12), 3: fr(1, 3), 4: fr(1, 3), 5: fr(1, 12), 6: fr(1, 12)}

    result = transform_random_variable(
        transform_random_variable(rv_1, get_const_rv(2), lambda a, b: a + b),
        transform_random_variable(rv_1, rv_2, lambda a, b: a * b),
        lcm
    )
    print(build_table(result))


if __name__ == '__main__':
    main()
