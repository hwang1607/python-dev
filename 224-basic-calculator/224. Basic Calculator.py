class Solution:
    def calculate(self, s: str) -> int:
        
        # Initialize the stack, current number, and sign
        stack = []
        currentNumber = 0
        sign = 1
        result = 0
        
        # Iterate over each character in the string
        for char in s:
            
            # If the character is a digit, build the current number
            if char.isdigit():
                currentNumber = currentNumber * 10 + int(char)
            
            # If the character is a plus or minus sign
            elif char in ['+', '-']:
                
                # Update the result with the current number and sign
                result += sign * currentNumber
                
                # Update the sign based on the current character
                sign = 1 if char == '+' else -1
                
                # Reset the current number
                currentNumber = 0
            
            # If the character is an opening parenthesis
            elif char == '(':
                
                # Push the result and sign onto the stack
                stack.append(result)
                stack.append(sign)
                
                # Reset the result and sign for the new sub-expression
                result = 0
                sign = 1
            
            # If the character is a closing parenthesis
            elif char == ')':
                
                # Update the result with the current number and sign
                result += sign * currentNumber
                
                # Pop the sign and previous result from the stack
                result *= stack.pop()
                result += stack.pop()
                
                # Reset the current number
                currentNumber = 0
        
        # Add the last number to the result
        result += sign * currentNumber
        
        return result