def solve():
    passport_keys = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid")
    passport = dict.fromkeys(passport_keys)

    with open('input.txt') as f:
        valid = 0

        for line in f:
            line = line.rstrip()

            if len(line) == 0:
                if sum(1 for key in passport.keys() if key != "cid" and passport[key] is None) == 0:
                    valid += 1

                passport = dict.fromkeys(passport_keys)
                continue

            key_values = line.split(" ")
            for pair in key_values:
                key, value = pair.split(":")
                passport[key] = value

        return valid


print(solve())
