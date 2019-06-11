import ast


def is_white_list_operators(node: ast.operator):
    if isinstance(node, ast.Mult):
        print('合法')


def get_operators(node: ast.AST):
    operators = []
    for field, value in ast.iter_fields(node):
        # white_list_operators(value)
        if isinstance(value, list):
            for item in value:
                if isinstance(item, ast.AST):
                    operators.extend(get_operators(item))
        elif isinstance(value, ast.AST):
            operators.extend(get_operators(value))
        if field == 'op':
            operators.append(value)
    return operators


def parse(syntax: str) -> [ast.operator]:
    return get_operators(ast.parse(syntax))
