#Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?

def find_pairs(arr, target_sum):
    pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                pairs.append((arr[i], arr[j]))
            
    return pairs

arr = [1, 2, 3, 4, 5]
target_sum = 7
result = find_pairs(arr, target_sum)
print(result)

#Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

def reverse_array(arr):
    start_index = 0
    end_index = len(arr) - 1
    while end_index > start_index:
        arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
        start_index += 1
        end_index -= 1

arr = [ 1,2,3,4,5]
reverse_array(arr)
print(arr)

#Q3. Write a program to check if two strings are a rotation of each other?

def are_rotations(str1, str2):
    if len(str1) != len(str2):
        return False
    temp = str1 + str1
    if str2 in temp:
        return True
    else:
        return False

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if are_rotations(str1, str2):
    print("The strings are rotations of each other.")
else:
    print("The strings are not rotations of each other.")

#Q4. Write a program to print the first non-repeated character from a string?

def first_non_repeated_character(string):
    # Create a dictionary to store the count of each character
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
   # Loop through the string again to find the first non-repeated character
    for char in string:
        if char_count[char] == 1:
            return char
    # If no non-repeated character is found, return None
    return None

string = input("Enter a string: ")

result = first_non_repeated_character(string)

if result is None:
    print("There are no non-repeated characters in the string.")
else:
    print("The first non-repeated character in the string is:", result)

#Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.

def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return
    tower_of_hanoi(n-1, source, auxiliary, destination)
    print("Move disk", n, "from", source, "to", destination)
    tower_of_hanoi(n-1, auxiliary, destination, source)

n = int(input("Enter the number of disks: "))
tower_of_hanoi(n, 'A', 'C', 'B')


#Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

def postfix_to_prefix(postfix):
    stack = []
    for char in postfix:
        if char.isalnum():
            stack.append(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            expression = char + operand2 + operand1
            stack.append(expression)
    return stack.pop()

postfix = input("Enter postfix expression: ")
prefix = postfix_to_prefix(postfix)
print("Prefix expression:", prefix)


#Q7. Write a program to convert prefix expression to infix expression.

def prefix_to_infix(prefix):
    stack = []
    for char in reversed(prefix):
        if char.isalnum():
            stack.append(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            expression = f"({operand1}{char}{operand2})"
            stack.append(expression)
    return stack.pop()

prefix = input("Enter prefix expression: ")
infix = prefix_to_infix(prefix)
print("Infix expression:", infix)


#Q8. Write a program to check if all the brackets are closed in a given code snippet.

def is_balanced(code):
    stack = []
    for char in code:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack:
                return False
            if char == ")" and stack[-1] != "(":
                return False
            if char == "]" and stack[-1] != "[":
                return False
            if char == "}" and stack[-1] != "{":
                return False
            stack.pop()
    return not stack

code = input("Enter a code snippet: ")
if is_balanced(code):
    print("All brackets are closed.")
else:
    print("All brackets are not closed.")


#Q9. Write a program to reverse a stack.

def reverse_stack(stack):
    if not stack:
        return
    temp = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, temp)

def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
        return
    temp = stack.pop()
    insert_at_bottom(stack, item)
    stack.append(temp)

stack = []
n = int(input("Enter the number of elements in the stack: "))
for i in range(n):
    stack.append(int(input(f"Enter element {i + 1}: ")))

print(f"Original stack: {stack}")
reverse_stack(stack)
print(f"Reversed stack: {stack}")



#Q10. Write a program to find the smallest number using a stack.

stack = []
n = int(input("Enter the number of elements in the stack: "))
for i in range(n):
    stack.append(int(input(f"Enter element {i + 1}: ")))

min_num = stack.pop()
while stack:
    num = stack.pop()
    if num < min_num:
        min_num = num

print(f"The smallest number is {min_num}")