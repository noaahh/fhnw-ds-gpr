def solve():
    passport_keys = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid")
    passport = dict.fromkeys(passport_keys)

    with open('input.txt') as f:
        valid = 0

        for line in f:
            line = line.rstrip()

            if len(line) == 0:
                valid += 1 if check_passport(passport) else 0
                passport = dict.fromkeys(passport_keys)
                continue

            key_values = line.split(" ")
            for pair in key_values:
                key, value = pair.split(":")
                passport[key] = value

        valid += check_passport(passport)
        return valid


def check_passport(passport):
    invalid = 0

    for key in passport.keys():
        if passport[key] is None:
            if key != "cid":
                return False
            continue

        try:
            int_val = int(passport[key])
        except ValueError:
            int_val = -1

        if key == "byr":
            invalid += 0 if 1920 <= int_val <= 2002 else 1

        elif key == "iyr":
            invalid += 0 if 2010 <= int_val <= 2020 else 1

        elif key == "eyr":
            invalid += 0 if 2020 <= int_val <= 2030 else 1

        elif key == "hgt":
            unit = passport[key][-2:]
            value = int(passport[key][:-2])
            invalid += 0 if (unit == "cm" and 150 <= value <= 193) or (unit == "in" and 59 <= value <= 76) else 1

        elif key == "hcl":
            allowed_chars = ["a", "b", "c", "d", "e", "f", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            invalid += 0 if passport[key][0] == "#" and len(passport[key]) == 7 and all(
                [char in allowed_chars for char in passport[key][1:]]) else 1

        elif key == "ecl":
            invalid += 0 if passport[key] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] else 1

        elif key == "pid":
            invalid += 0 if len(passport[key]) == 9 and int_val != -1 else 1

        if invalid != 0:
            return False

    return True


print(solve())
