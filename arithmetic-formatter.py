def arithmetic_arranger(problems, show_answers=False):
    # Check if too many problems are supplied max 5 allowed
    if len(problems) > 5:
        return "Error: Too many problems."

    # Lists to hold each line of the arranged problems
    first_line = []    
    second_line = []   
    dashes_line = []   
    answers_line = []  #if show_answers is True

    for problem in problems:
        # Split problem into parts: number1, operator, number2
        parts = problem.split()
        
        # If problem does not have exactly 3 parts return error
        if len(parts) != 3:
            return "Error: Invalid problem format."

        num1, operator, num2 = parts

        # Check that operator is '+' or '-'
        if operator not in ("+", "-"):
            return "Error: Operator must be '+' or '-'."

        # Check that both operands contain digits only
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."

        # Check that operands are not more than 4 digits long
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate the width needed for formatting each problem:
        # Width = length of the longer operand + 2 spaces for operator and space
        width = max(len(num1), len(num2)) + 2

        # Format the top number, right aligned
        first_line.append(num1.rjust(width))

        # Format the operator and bottom number, operator on left bottom number right aligned
        second_line.append(operator + " " + num2.rjust(width - 2))

        # Add a line of dashes, same length as width
        dashes_line.append("-" * width)

        # If answers should be shown calculate and format the result
        if show_answers:
            if operator == "+":
                answer = str(int(num1) + int(num2))
            else:  # operator == "-"
                answer = str(int(num1) - int(num2))
            # Right align the answer within the width
            answers_line.append(answer.rjust(width))

    # Join each line's problems with 4 spaces between them
    arranged_first = "    ".join(first_line)
    arranged_second = "    ".join(second_line)
    arranged_dashes = "    ".join(dashes_line)

    # If showing answers join and add the answers line as well
    if show_answers:
        arranged_answers = "    ".join(answers_line)
        return f"{arranged_first}\n{arranged_second}\n{arranged_dashes}\n{arranged_answers}"
    else:
        # otherwise, just return the first three lines
        return f"{arranged_first}\n{arranged_second}\n{arranged_dashes}"


# Example usage - these print the arranged problems:

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print() 
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
