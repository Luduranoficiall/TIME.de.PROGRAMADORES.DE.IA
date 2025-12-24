// Exemplo Node.js usando fengari (Lua VM para JS)
// Instale: npm install fengari
const { lua, to_jsstring, to_luastring } = require('fengari');
const { luaL_dostring, luaL_newstate, luaL_openlibs } = require('fengari/src/lauxlib.js');

const L = luaL_newstate();
luaL_openlibs(L);
luaL_dostring(L, to_luastring('print("Olá do Lua rodando no Node.js!")'));
