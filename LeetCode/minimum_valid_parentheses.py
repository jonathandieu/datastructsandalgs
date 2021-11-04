def minimum_valid_parentheses(s: string) -> string:
   stack = []
        s = list(s)
        # Iterate through the string and check for parentheses
        for index, char in enumerate(s):
            # If the character is an open parenthesis:
            if char == '(':
                stack.append(index) # append the index to the stack
            # If the char is a closing parenthesis:
            if char == ')':
                if len(stack) != 0: # when the stack has elements, we pop from the stack and it remains valid
                    stack.pop()
                    continue # make sure we continue after popping because we don't want to check if the stack is empty on the same iteration
                if stack == []:
                    s[index] = ""
        for index in stack:
            s[index] = ''
        return "".join(s)