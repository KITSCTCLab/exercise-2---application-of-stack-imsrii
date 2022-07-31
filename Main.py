def evaluate_postfix_expression(self, expression):
    """
    Evaluate the postfix expression
    Arguments:
      expression: A String which represents the the expression to be evaluated
    Returns:
      The result of evaluated postfix expression.
    """
    self.stack = []
    for element in expression:
      if element.isdigit():
        self.push(int(element))
      elif element in ["+", "-", "*", "/", "^"]:
        if element == "+":
          result = self.stack[-2] + self.stack[-1]
        elif element == "-":
          result = self.stack[-2] - self.stack[-1]
        elif element == "*":
          result = self.stack[-2] * self.stack[-1]
        elif element == "/":
          result = self.stack[-2] // self.stack[-1]
        elif element == "^":
          result = self.stack[-2] ** self.stack[-1]
        self.pop()
        self.pop()
        self.push(result)
    return self.pop()

# Do not change the following code
postfix_expression = input()  # Read postfix expression
tokens = postfix_expression.split()
evaluate = Evaluate(len(tokens))
if evaluate.validate_postfix_expression(tokens):
    print(evaluate.evaluate_postfix_expression(tokens))
else:
    print('Invalid postfix expression')
