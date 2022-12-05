def solve():
    passport_keys = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid")
    passport = dict.fromkeys(passport_keys)

    with open('input.txt') as f:
        valid = 0

        for line in f:
            line = line.rstrip()

            if len(line) == 0:
                valid += check_passport(passport)
                passport = dict.fromkeys(passport_keys)
                continue

            key_values = line.split(" ")
            for pair in key_values:
                key, value = pair.split(":")
                passport[key] = value

        valid += check_passport(passport)
        return valid


def check_passport(passport):
    return 1 if sum(1 for key in passport.keys() if passport[key] is None and key != "cid") == 0 else 0


print(solve())
