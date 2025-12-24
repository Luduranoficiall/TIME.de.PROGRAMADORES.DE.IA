-- Simulação de automação IoT em Lua
function ler_sensor()
    local valor = math.random(0, 100)
    print("Valor do sensor:", valor)
    return valor
end

function acionar_atuador(valor)
    if valor > 50 then
        print("Atuador LIGADO")
    else
        print("Atuador DESLIGADO")
    end
end

local v = ler_sensor()
acionar_atuador(v)
