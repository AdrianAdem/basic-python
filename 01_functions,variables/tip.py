def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    strip_dollars = d.strip("$##")
    return float(strip_dollars)


def percent_to_float(p):
    strip_percent = p.strip("##%")
    return float(strip_percent) / 100


main() 