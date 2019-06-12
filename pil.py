import ast


white_list = [ast.Module, ast.Store, ast.Expr, ast.Assign,
              ast.BinOp, ast.Num, ast.Name, ast.stmt, ast.operator, ast.Load]


def white_list_validator(node):
    throw_flag = True
    for n in ast.walk(node):
        for item in white_list:
            if isinstance(n, item):
                throw_flag = False
                break
        if throw_flag:
            raise Exception('Illegal node: {}'.format(type(n).__name__))
        throw_flag = True


# Get operators from AST nodes
def get_operators(node: ast.AST):
    operators = []
    for n in ast.walk(node):
        for field, value in ast.iter_fields(n):
            if field == 'op':
                operators.append(value)
    return operators


# parse syntax string to AST by ast lib, and return list of operator in AST.
def parse(syntax: str) -> [ast.operator]:
    return get_operators(ast.parse(syntax))
