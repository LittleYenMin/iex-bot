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


# parse syntax string to AST by ast lib, and return list of operator in AST.
def parse(syntax: str) -> [ast.operator]:
    node = ast.parse(syntax)
    white_list_validator(node)


# is_white_list_operators(None)
print(white_list_validator(ast.parse('a/=10')))
print(white_list_validator(ast.parse('a=10')))
print(white_list_validator(ast.parse('ast.dump(node)')))
print(white_list_validator(ast.parse('import ast')))
# print(parse('a = 100/5'))
# print(parse('ast.dump(node)'))
