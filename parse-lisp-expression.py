class Solution:
    def evaluate(self, expression: str) -> int:
        SCOPE = []
        def tokenize(s):
            i = 0
            left = 0
            for j in range(len(s)):
                if left == 0 and s[j] == " ":
                    yield s[i:j]
                    i = j + 1
                elif s[j] in "()":
                    if s[j] == "(":
                        left += 1
                    elif s[j] == ")":
                        left -= 1
            yield s[i:]

        def is_variable(s):
            return s[0].isalpha()

        def is_number(s):
            if s[0] == "-":
                return s[1:].isnumeric()
            else:
                return s.isnumeric()

        def get_variable(var):
            for namespace in reversed(SCOPE):
                if namespace.get(var) is not None:
                    return namespace[var]
        def add_variable(var, value):
            SCOPE[-1][var] = value
        def eval(s):
            SCOPE.append({})
            tokens = list(tokenize(s))
            if len(tokens) == 1:
                s = tokens[0]
                if s[0] == "(" and s[-1] == ")":
                    res = eval(s[1:-1])
                elif is_number(s):
                    res = int(s)
                elif is_variable(s):
                    res = get_variable(s)
            else:
                op = tokens[0]
                if op == "add":
                    v1 = eval(tokens[1])
                    v2 = eval(tokens[2])
                    res = v1 + v2
                elif op == "mult":
                    v1 = eval(tokens[1])
                    v2 = eval(tokens[2])
                    res = v1 * v2
                elif op == "let":
                    for i in range(1, len(tokens), 2):
                        kv = tokens[i:i+2]
                        if len(kv) == 2:
                            var, val = kv
                            add_variable(var, eval(val))
                        else:
                            res = eval(kv[0])
            SCOPE.pop()
            return res
        return eval(expression)