// Exemplo de binding C para Lua (usando Lua 5.3+)
// Compile com: gcc -o exemplo_c_lua exemplo.c -llua5.3
#include <lua.h>
#include <lauxlib.h>
#include <lualib.h>
#include <stdio.h>

int c_soma(lua_State *L) {
    int a = luaL_checkinteger(L, 1);
    int b = luaL_checkinteger(L, 2);
    lua_pushinteger(L, a + b);
    return 1;
}

int main() {
    lua_State *L = luaL_newstate();
    luaL_openlibs(L);
    lua_register(L, "c_soma", c_soma);
    luaL_dostring(L, "print('Soma em C chamada do Lua:', c_soma(10, 20))");
    lua_close(L);
    return 0;
}
