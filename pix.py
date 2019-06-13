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
            raise ValueError('Illegal node: {}'.format(type(n).__name__))
        throw_flag = True


# parse syntax string to AST by ast lib, and return list of operator in AST.
def parse(syntax: str) -> [ast.operator]:
    try:
        node = ast.parse(syntax)
        white_list_validator(node)
    except Exception:
        raise
