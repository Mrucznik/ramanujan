from fractions import Fraction
import matplotlib.pyplot as plt


def base_func(x):
    # podstawowa funkcja dająca ciąg: 1, -1, 1, -1...
    return pow(-1, x)
    # interesujące, że przy takiej funkcji dostaniemy
    # ciąg średnich średnich zbieżny do 1/2. Czy zatem
    # wykonywanie średniej ciągu i dodanie 1 jest odwrotnością
    # mnożenia przez nieskończoną liczbę elementów?
    # poprawka: podówjna średnia (avgs_of_avgs_wrong) daje 1/2
    # return 1+x*pow(-1, x)
    # funkcja dająca ciąg 1, -2, 3, -4...
    # return (x+1)*pow(-1, x)

def get_base_series(n):
    for x in range(n):
        yield base_func(x)


def get_sums(n, series=get_base_series):
    sum = 0
    for x in series(n):
        sum += x
        yield sum


def get_sum_of_sums(n):
    sum = 0
    for x in get_sums(n):
        sum += x
        yield sum


def get_avgs(n):
    count = 0
    for x in get_sums(n, get_sums):
        count += 1
        yield x / count


# wrong, but also interesting
def get_avgs_of_avgs_wrong(n):
    count = 0
    for x in get_avgs(n):
        count += 1
        yield x / count


def get_avgs_of_avgs(n):
    count = 0
    for x in get_sums(n, get_avgs):
        count += 1
        yield x / count


def print_func(func):
    for sum in func:
        # print(Fraction(sum).limit_denominator(), end = ', ')
        print(sum)


def plot_func(func, title="Wyniki"):
    vals = list(func)
    plt.plot(vals)
    plt.ylabel(title)
    plt.show()
    print(title)
    print_func(vals)


plot_func(get_base_series(50), "Base func")
plot_func(get_sums(50), "Sums")
plot_func(get_sums(50, get_sums), "Sum of sums")
plot_func(get_avgs(50), "Averages")
plot_func(get_avgs_of_avgs(50), "Averages of averages")
print("\nok")

# def avg1(i):
#     sum = 0
#     for x in range(0, i):
#         sum += (pow(-1, x)+1)/2
#     return sum / (i+1)

# def avg2(i):
#     sum = 0
#     for x in range(0, i):
#         sum += avg1(x)
#     return sum / (i+1)

# def series1(n):
#     avgs = [0] * n
#     for i in range(0, n):
#         avgs[i] = avg1(i)
#     return avgs

# def series2(n):
#     avgs = [0] * n
#     for i in range(0, n):
#         avgs[i] = avg2(i)
#     return avgs

# print("Seria 1:")
# for value in series1(25):
#     print(Fraction(value).limit_denominator())

# print("Seria 2:")
# for value in series2(100):
#     print(Fraction(value).limit_denominator())