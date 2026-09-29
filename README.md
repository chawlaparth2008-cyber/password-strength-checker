# Password Strength Checker — Project Statement

## Purpose

This project is a beginner-friendly Python command-line program that evaluates a password against five simple composition requirements and reports which requirements are met.

## Scope

The checker evaluates whether the entered text:

1. Contains at least 15 characters.
2. Contains at least one digit.
3. Contains at least one uppercase letter.
4. Contains at least one lowercase letter.
5. Contains at least one configured special character from `!@#$%^&*()-_=+[];:,`.

It reports the number of requirements met, provides a simple strength label, and suggests any unmet requirements. It checks one entry and then exits. The project uses Python's standard library and requires Python 3.

## Strength labels

- **Weak:** The input is shorter than 15 characters, or no more than two requirements are met.
- **Medium:** The input is at least 15 characters long and three or four requirements are met.
- **Strong:** The input is at least 15 characters long and all five requirements are met.

## Limitations and safe use

These labels reflect only the project's five rules. They do not establish real-world password security or check whether a password is common or compromised. The program does not intentionally save the entered value or send it to a network service, but terminal input is visible while typing. Use fictional sample passwords only; do not enter a real password.

## How to run

From the project folder, run:

```bash
python passwordstrengthchecker.py
```

On some systems, use `python3` instead of `python`.
