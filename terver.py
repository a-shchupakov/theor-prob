from fractions import Fraction as fr
from matplotlib import pyplot as plot


DIGITS = 4


def build_table(random_variable):
    result = ''
    for k, v in sorted(random_variable.items()):
        result += '{} -> {}\r\n'.format(str(int(k)), str(v))
    return result


def get_const_rv(value):
    return {value: 1}


def get_expected_value(random_variable):
    exp_value = 0
    for k, v in random_variable.items():
        exp_value += k * v

    return round(exp_value, DIGITS)


def get_squared_random_variable(random_variable):
    new_rv = {}
    for k1, v1 in random_variable.items():
        key = k1 * k1
        if key not in new_rv:
            new_rv[key] = 0
        new_rv[key] += v1

    return new_rv


def get_dispersion(random_variable):
    t1 = get_expected_value(get_squared_random_variable(random_variable))
    t2 = get_expected_value(random_variable) ** 2
    return round(t1 - t2, DIGITS)


def build_distribution_function(random_variable):
    result = {}
    current_prob = 0

    # P(X <= k)
    for k, v in sorted(random_variable.items()):
        current_prob += v
        result[k] = current_prob

    return result


def get_median(random_variable):
    d_function = build_distribution_function(random_variable)
    for x, y in sorted(d_function.items()):
        if y >= 0.5 and 1 - y + random_variable[x]:
            return x


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

    theta = transform_random_variable(
        transform_random_variable(rv_1, get_const_rv(2), lambda a, b: a + b),
        transform_random_variable(rv_1, rv_2, lambda a, b: a * b),
        lcm
    )

    print(build_table(theta))
    print('Expected value: ' + str(get_expected_value(theta)))
    print('Dispersion: ' + str(get_dispersion(theta)))

    func = build_distribution_function(theta)
    x, y = zip(*func.items())
    plot.plot(x, y)
    plot.xlabel('Значение величины')
    plot.ylabel('Вероятность')

    plot.show()




if __name__ == '__main__':
    main()
