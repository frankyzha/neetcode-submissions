class Solution:
    def isValid(self, s: str) -> bool:
        close2open = {
            ')': "(",
            '}': '{',
            ']': '['
        }
        open_brackets = []
        for c in s:
            if c in close2open.values():
                open_brackets.append(c)
            else:
                if not open_brackets:
                    return False
                last_bracket = open_brackets.pop()
                if last_bracket != close2open[c]:
                    return False
        return not open_brackets