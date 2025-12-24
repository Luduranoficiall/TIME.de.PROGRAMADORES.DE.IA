# Exemplo bidirecional: Python chama Lua e Lua chama Python
from lupa import LuaRuntime

def py_multiplica(a, b):
    print(f"Multiplicando em Python: {a} * {b}")
    return a * b

lua = LuaRuntime(unpack_returned_tuples=True)
lua.globals()['py_multiplica'] = py_multiplica

lua_code = '''
function soma_e_multiplica(a, b)
    local soma = a + b
    local mult = py_multiplica(a, b)
    return soma, mult
end
'''
lua.execute(lua_code)

soma_e_multiplica = lua.eval('soma_e_multiplica')
soma, mult = soma_e_multiplica(3, 7)
print(f"Soma em Lua: {soma}")
print(f"Multiplicação em Python (chamada pelo Lua): {mult}")
