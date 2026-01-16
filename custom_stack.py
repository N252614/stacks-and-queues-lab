def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.
    """
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        # If it's an opening bracket, push it onto the stack
        if ch in pairs.values():
            stack.append(ch)

        # If it's a closing bracket, it must match the stack top
        elif ch in pairs:
            if not stack:
                return False
            top = stack.pop()
            if top != pairs[ch]:
                return False

        # If other characters appear, ignore them 
        else:
            continue

    # If stack is empty, all brackets were matched
    return len(stack) == 0
