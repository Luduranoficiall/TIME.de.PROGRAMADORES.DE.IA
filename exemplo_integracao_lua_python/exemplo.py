# Exemplo de integração Python + Lua usando lupa
# Requer: pip install lupa
from lupa import LuaRuntime

# Carrega o script Lua
with open('exemplo_integracao_lua_python/exemplo.lua', 'r') as f:
    lua_code = f.read()

lua = LuaRuntime(unpack_returned_tuples=True)
lua.execute(lua_code)

# Chama a função soma definida no Lua
soma = lua.eval('soma')
resultado = soma(10, 5)
print(f'Resultado da soma em Lua: {resultado}')
