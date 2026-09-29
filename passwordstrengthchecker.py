def digit_found(password):
    for ch in password:
        if ch.isdigit():
            return True

    return False


def uppercase_found(password):
    for ch in password:
        if ch.isupper():
            return True

    return False


def lowercase_found(password):
    for ch in password:
        if ch.islower():
            return True

    return False


def special_found(password):
    special_chars = "!@#$%^&*()-_=+[];:,"

    for ch in password:
        if ch in special_chars:
            return True

    return False


def minimunlength_found(password):
    if len(password) >= 15:
        return True

    return False


def get_password_length(password):
    return len(password)


def get_all_rule_results(password):
    results = []

    results.append(minimunlength_found(password))
    results.append(digit_found(password))
    results.append(uppercase_found(password))
    results.append(lowercase_found(password))
    results.append(special_found(password))

    return results


def count_passed_rules(results):
    count = 0

    for result in results:
        if result:
            count += 1

    return count


def get_strength(password, count):
    if len(password) < 15:
        return "weak"

    if count <= 2:
        return "weak"

    if count <= 4:
        return "medium"

    return "strong"


def print_header():
    print()
    print("password check results")
    print("----------------------")


def print_password_length(password):
    print("password length:", get_password_length(password))


def print_score(count):
    print("requirements met:", count, "out of 5")


def print_strength(password, count):
    strength = get_strength(password, count)
    print("password strength:", strength)


def print_rule_result(rule_name, passed):
    if passed:
        print("[PASS]", rule_name)
    else:
        print("[NEEDS WORK]", rule_name)


def print_all_rule_results(password):
    print()
    print("Requirement details:")
    print_rule_result("at least 15 characters", minimunlength_found(password))
    print_rule_result("contains a digit", digit_found(password))
    print_rule_result("contains an uppercase letter", uppercase_found(password))
    print_rule_result("contains a lowercase letter", lowercase_found(password))
    print_rule_result("contains a special character", special_found(password))


def print_length_suggestion(password):
    if not minimunlength_found(password):
        print("- Use at least 15 characters.")


def print_digit_suggestion(password):
    if not digit_found(password):
        print("- Add a digit, such as 4 or 8.")


def print_uppercase_suggestion(password):
    if not uppercase_found(password):
        print("- Add an uppercase letter, such as A or B.")


def print_lowercase_suggestion(password):
    if not lowercase_found(password):
        print("- Add a lowercase letter, such as a or b.")


def print_special_suggestion(password):
    if not special_found(password):
        print("- Add a special character, such as ! or #.")


def print_suggestions(password):
    print()
    print("suggestions:")

    print_length_suggestion(password)
    print_digit_suggestion(password)
    print_uppercase_suggestion(password)
    print_lowercase_suggestion(password)
    print_special_suggestion(password)


def print_success_message(count):
    if count == 5:
        print()
        print("your password meets all the requirements!")


def print_empty_password_message():
    print("you did not enter a password.")
    print("run the program again and enter a password to check.")


def print_privacy_message():
    print("your password is checked only by this program.")
    print("do not share your real password with other people.")


def check_password(password):
    if password == "":
        print_empty_password_message()
        return

    results = get_all_rule_results(password)
    count = count_passed_rules(results)

    print_header()
    print_password_length(password)
    print_score(count)
    print_strength(password, count)
    print_all_rule_results(password)
    print_suggestions(password)
    print_success_message(count)
    print()
    print_privacy_message()


def get_password_from_user():
    return input("enter a password to check: ")


def main():
    print("password strength checker")
    print("=========================")
    print("Enter one password to check its strength.")
    print()

    password = get_password_from_user()
    check_password(password)


if __name__ == "__main__":
    main()


