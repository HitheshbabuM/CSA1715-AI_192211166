from itertools import permutations

def solve_cryptarithmetic(words):
    puzzle = ' + '.join(words[:-1]) + ' == ' + words[-1]
    letters = set(char for word in words for char in word if char.isalpha())

    if len(letters) > 10:
        return "Invalid puzzle: More than 10 distinct letters."

    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        equation = ''.join(str(mapping[char]) if char.isalpha() else char for char in puzzle)
        if not any(part.startswith('0') and len(part) > 1 for part in equation.split()) and eval(equation):
            return mapping

    return "No solution found."

# Example usage:
words_input = input("Enter the words of the Cryptarithmetic puzzle separated by spaces: ").split()
solution = solve_cryptarithmetic(words_input)
if isinstance(solution, dict):
    print("Solution found:")
    for char, digit in solution.items():
        print(f"{char} = {digit}")
else:
    print(solution)
