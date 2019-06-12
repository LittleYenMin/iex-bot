import ast


def is_white_list_operators(node: ast.operator):
    if isinstance(node, ast.Mult):
        print('合法')


# Get operators from AST nodes
def get_operators(node: ast.AST):
    operators = []
    for field, value in ast.iter_fields(node):
        if isinstance(value, list):
            for item in value:
                if isinstance(item, ast.AST):
                    operators.extend(get_operators(item))
        elif isinstance(value, ast.AST):
            operators.extend(get_operators(value))
        if field == 'op':
            operators.append(value)
    return operators


# parse syntax string to AST by ast lib, and return list of operator in AST.
def parse(syntax: str) -> [ast.operator]:
    return get_operators(ast.parse(syntax))
