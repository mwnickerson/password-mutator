# Password Mutator Script

## Description

The Password Mutator Script is a Python tool designed to generate various mutations of a weak password. It performs transformations such as capitalization, symbol substitutions, and appending common number and year suffixes. This tool can be useful for testing password strength and populating azure's banned word list. 

## Features

- Capitalizes letters in various combinations.
- Converts the password to uppercase and lowercase.
- Substitutes common letters with symbols (e.g., 'a' -> '@').
- Appends common suffixes including numbers and years.
- Outputs the mutations to a specified text file.

## Requirements

- Python 3.x installed on your system.

## Installation

1. **Install Python**: If you don't have Python installed, download and install it from [python.org](https://www.python.org/downloads/).

2. **Download the Script**: Save the script as `password_mutator.py`.

3. **Open a Terminal or Command Prompt**: Navigate to the directory where you saved the script.

## Usage

To run the script, use the following command in your terminal or command prompt:
```
python password_mutator.py <your_weak_password> [output_file.txt]
````

### Parameters

- `<your_weak_password>`: The weak password you want to mutate.
- `[output_file.txt]`: (Optional) The name of the output file where the mutations will be saved. If not provided, the output file will be named `<your_weak_password>.txt`.

### Example

1. To generate mutations for the password "password" and save them to a file named `password.txt`:

```
 python password_mutator.py password
 ```

2. To generate mutations for the password "password" and save them to a file named `custom_output.txt`:

```
 python password_mutator.py password custom_output.txt 
 ```


## Output

The script will create a text file containing all the generated mutations of the specified password. Each mutation will be listed on a new line.

## Disclaimer

This tool is intended for educational purposes only. Please use it responsibly and ethically. Do not use this script to test passwords that do not belong to you or without permission.




