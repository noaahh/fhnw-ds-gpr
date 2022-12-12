def kaprekar(num):
    str_num = str(num)
    if num < 1000:
        str_num = "".join(["0" for i in range(4 - len(str_num))]) + str_num

    z = str_num
    while z != num and z != 6174:
        z = int("".join(sorted(str(z), reverse=True))) - int("".join(sorted(str(z))))

    return z


def rotate_left_str(s, n):
    return s if len(s) < n else s[n:] + s[:n]


def move2_str(s):
    even, odd = [], []
    for i in range(len(s)):
        even.append(s[i]) if i % 2 == 0 else odd.append(s[i])

    return "".join(odd) + "".join(even)


def str_count(string, pattern):
    counter = 0
    for i in range(len(string)):
        if i + 1 >= len(pattern):
            if string[i + 1 - len(pattern):i + 1] == pattern:
                counter = counter + 1

    return counter


def str_count_any(string, pattern):
    return sum([1 for i in range(len(string)) for p in pattern if string[i] == p])


def max_index(lst):
    largest = -1
    for i in range(len(lst)):
        largest = i if lst[largest] <= lst[i] else largest

    return largest


def string_decomposition(s):
    blank_splits = s.split(" ")
    num1, num2 = blank_splits[0].split("-")
    return num1, num2, blank_splits[1][0], blank_splits[2]


def i_squared_mod5_is4(n):
    return [i for i in range(n) if (i ** 2 % 5) == 4]


if __name__ == '__main__':
    print(rotate_left_str("abcdefgh", 3))
    print(move2_str("abcdefgh"))

    print(str_count("Das ist ein netter Verersucher", "er"))
    print(str_count_any("Das ist ein netter Versuch", "er"))

    print(max_index([1, 4, 100, 100, 4]))

    print(string_decomposition("32-165 k: sdklffs"))

    print(i_squared_mod5_is4(1000))
