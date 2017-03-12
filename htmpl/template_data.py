import re


class TemplateData:
    def __init__(self, data: dict, root, path):
        self.data = data
        self.root = root
        self.path = path

    def bind(self, key, value):
        self.data[key] = value

    def evaluate(self, expression: str):
        for variable in re.findall('\$[a-zA-Z()\->$]+', expression):
            expression = expression.replace(variable, str(self.resolve(variable)))
        return eval(expression)

    def resolve(self, expression: str, throw: bool = False) -> object:
        if expression.startswith('eval('):
            return self.evaluate(expression[5:-1])

        if not expression[0] == '$':
            return expression

        variable = expression[1:]

        tokens = re.split('[()]', variable)
        for index, token in enumerate(tokens):
            if token == '':
                continue
            if token[0] == '$':
                tokens[index] = self.resolve(token, throw)
        variable = ''.join(tokens)

        thing = self.data
        for token in variable.split('->'):
            if token in thing:
                thing = thing[token]
            else:
                if throw:
                    raise ValueError(f'Unable to resolve variable: {variable}')
                else:
                    return ''
        return thing
