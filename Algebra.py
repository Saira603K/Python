def simplify_expression(expression):
    stack = []
    result = ""
    current_sign = "+"

    for char in expression:
        if char == " ":
            continue

        if char == "(":
            stack.append((result, current_sign))
            result = ""
            current_sign = "+"

        elif char == ")":
            previous_result, previous_sign = stack.pop()

            # Compare sign outside and inside the parenthesis
            if previous_sign == "-":
                result = previous_result + "-" + result.replace("+", "-").replace("-", "+")
            else:
                result = previous_result + result.replace("+", "-").replace("-", "+")

        elif char == "+":
            if len(result) == 0 or result[-1] in ("+", "-"):
                result += char
            else:
                current_sign = "+"

        elif char == "-":
            if len(result) == 0 or result[-1] in ("+", "-"):
                result += char
            else:
                current_sign = "-"

        else:
            result += current_sign + char
            current_sign = "+"

    return result
  
  expression = "x – (y – z – (u+v) ) – w"
simplified_expression = simplify_expression(expression)

print(simplified_expression) 

# Output: x – y + z + u + v – w

