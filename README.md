# Password Strength Checker & Generator

A simple Python program that allows users to either **check the strength of a password** or **generate a random strong password** based on selectable character options.

---

## Features

- ✔️ Password strength validation  
- ✔️ Customizable random password generation  
- ✔️ Interactive command-line interface  
- ✔️ Uses only built-in Python modules  

---

## How It Works

When running the script, you will be asked to choose between:

| Option | Action |
|--------|--------|
| `1` | Enter your own password to check its strength |
| `2` | Generate a random password |

---

## Password Strength Rules

A password is considered **strong** if it meets the following criteria:

- At least **8 characters long**
- Contains **uppercase letters**
- Contains **lowercase letters**
- Contains at least one special symbol (`@` or `_`)

If one or more rules are not met, the program will display helpful suggestions.

---

## Password Generator Options

When choosing password generation mode, you can decide which character sets to include:

- Digits
- Letters
- Special characters

You also choose the password length.

---

## Requirements

No external libraries required — only built-in modules:

- `random`
- `string`

---

## Running the Script

Use the following command:
`python main.py`

---

## License

This project is released under the **MIT License**.

---

## Support

If you like this project, feel free to **star the repository on GitHub!**
