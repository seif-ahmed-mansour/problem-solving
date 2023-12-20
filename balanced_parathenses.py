def balanced_parathenses(s):
    stack=[]
    for char in s:
        if char in ["(","{","["]:
            stack.append(char)
        else:
            if not stack:
                return "unbalanced"
            current_char=stack.pop()
            if current_char=="(":
                if char!=")":
                    return "unbalanced"
            if current_char=="{":
                if char!="}":
                    return "unbalanced"
            if current_char=="[":
                if char!="]":
                    return "unbalanced"
    if stack:
        return "unbalanced"
    return "balanced"


