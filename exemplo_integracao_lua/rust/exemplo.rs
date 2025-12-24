// Exemplo Rust usando rlua
// Adicione ao Cargo.toml: rlua = "*"
use rlua::Lua;

fn main() {
    let lua = Lua::new();
    lua.context(|ctx| {
        ctx.load("print('Olá do Lua rodando no Rust!')").exec().unwrap();
    });
}
