// Exemplo Go usando gopher-lua
// Instale: go get github.com/yuin/gopher-lua
package main
import (
	"github.com/yuin/gopher-lua"
)

func main() {
	L := lua.NewState()
	defer L.Close()
	L.DoString(`print('Olá do Lua rodando no Go!')`)
}
