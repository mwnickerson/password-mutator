import itertools
import argparse
import os

def mutate_password(password):
    mutations = []
    
    # Function to capitalize each letter in the password
    def capitalize_variations(word):
        return [''.join(c.upper() if i == j else c.lower() for i, c in enumerate(word)) 
                for j in range(len(word) + 1)]

    # Basic mutations
    mutations.extend(capitalize_variations(password))
    mutations.append(password.upper())
    mutations.append(password.lower())

    # Common letter-to-symbol substitutions
    substitutions = {
        'a': '@', 'A': '@',
        'e': '3', 'E': '3',
        'i': '1', 'I': '1',
        'o': '0', 'O': '0',
        's': '$', 'S': '$',
        't': '7', 'T': '7'
    }

    # Apply substitutions
    for i in range(1, len(password) + 1):
        for combo in itertools.combinations(range(len(password)), i):
            new_pass = list(password)
            for pos in combo:
                if new_pass[pos] in substitutions:
                    new_pass[pos] = substitutions[new_pass[pos]]
            mutations.append(''.join(new_pass))

    # Add common suffixes
    common_suffixes = ['123', '!', '!!', '?', '??', '.', '1', '12', '1234', '12345', '123456', '1234567', '12345678', '0', '01', '02']
    mutations.extend([password + suffix for suffix in common_suffixes])

    # Add year suffixes
    current_year = 2024
    for year in range(current_year - 5, current_year + 6):
        mutations.append(f"{password}{year}")

    # Remove duplicates and return
    return list(set(mutations))

def main():
    parser = argparse.ArgumentParser(description="Mutate a weak password using letters and symbols.")
    parser.add_argument("password", type=str, help="The weak password to mutate")
    parser.add_argument("output_file", type=str, nargs='?', default=None, help="The output file to save the mutations (optional)")
    args = parser.parse_args()

    weak_password = args.password
    output_file = args.output_file or f"{weak_password}.txt"
    
    # Ensure the output file name is safe
    output_file = "".join([c if c.isalnum() else "_" for c in output_file])

    mutated_passwords = mutate_password(weak_password)

    with open(output_file, 'w') as f:
        for mutation in mutated_passwords:
            f.write(mutation + '\n')

    print(f"Original password: {weak_password}")
    print(f"Number of mutations: {len(mutated_passwords)}")
    print(f"Mutations have been saved to {output_file}")

if __name__ == "__main__":
    main()
