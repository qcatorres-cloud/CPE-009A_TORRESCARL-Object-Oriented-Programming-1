def generate_truthtable(number_of_variables=0):
    if number_of_variables == 0:
        return "You need to enter an integer"
    else:
        total_combinations = 2**number_of_variables
        combinations_list = []
        for i in range(total_combinations):
            bin_equivalent = bin(i)[2:]   # binary string without '0b'
            while len(bin_equivalent) < number_of_variables:
                bin_equivalent = "0" + bin_equivalent
            combinations_list.append(tuple(int(val) for val in bin_equivalent))
        return combinations_list


def evaluate_propositional_logic(truthtable):
    # Example: evaluate (A AND B) OR C for 3 variables
    print("Evaluating (A AND B) OR C")
    print("A B C | Result")
    print("----------------")
    for row in truthtable:
        A, B, C = row
        result = (A and B) or C
        print(f"{A} {B} {C} |   {int(result)}")


# Run the program
print(generate_truthtable(3))  # Shows the raw truth table
evaluate_propositional_logic(generate_truthtable(3))  # Evaluates the logic