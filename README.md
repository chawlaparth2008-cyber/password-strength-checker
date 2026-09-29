# Password Strength Checker

A beginner-friendly Python command-line project that checks a password against five composition rules and prints the results with suggestions for any rules it does not meet.

## Features

- Checks for a minimum length of 15 characters
- Checks for at least one digit, uppercase letter, lowercase letter, and configured special character
- Shows the number of requirements met and a simple strength label
- Suggests which requirements are missing
- Uses Python's standard library; no extra packages are required

The special characters recognized by this version are: `!@#$%^&*()-_=+[];:,`.

## Requirements

- Python 3

## Run the project

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python passwordstrengthchecker.py
   ```

   On some systems, use `python3` instead of `python`.
4. Enter a sample password when prompted. The program checks one entry and then exits.

## Strength labels

- **Weak:** fewer than 15 characters, or at most 2 of the 5 rules pass
- **Medium:** at least 15 characters and 3 or 4 rules pass
- **Strong:** at least 15 characters and all 5 rules pass

These labels are based only on this project's rules. They are not a reliable measure of real-world password security and do not check for common or compromised passwords.

## Privacy and safe use

The program does not intentionally save the entered value to a file or send it to a network service. However, it uses ordinary terminal input, and this is an educational demonstration rather than a security product. Use a fictional sample; do not enter a real password.

## Testing

Try fictional inputs that cover the following cases:

- Empty input
- Fewer than 15 characters
- A 15-character-or-longer input missing one rule at a time
- An input meeting all five rules

The output should show each rule's result and suggestions for rules that were not met.

## Project files

- `passwordstrengthchecker.py` - Python source code for the checker
- `README.md` - Project overview and instructions

## License

No license has been selected for this project.
