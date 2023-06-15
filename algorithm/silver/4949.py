import sys

def is_balanced(expression):
    stack = []
    opening_brackets = ['(', '[']
    closing_brackets = [')', ']']

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            top = stack.pop()
            if opening_brackets.index(top) != closing_brackets.index(char):
                return False

    return len(stack) == 0

while True:
    line = sys.stdin.readline().rstrip()  # 한 줄을 입력받고 공백 제거
    if line == '.':
        break

    if is_balanced(line):
        print('yes')
    else:
        print('no')
