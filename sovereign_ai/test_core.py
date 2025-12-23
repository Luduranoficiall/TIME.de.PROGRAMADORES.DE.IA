from core import SovereignCore

def test_exec():
    core = SovereignCore("tenant_test")
    result = core.execute("Criar API REST em FastAPI")
    assert "output" in result
    assert result["score"] >= 0
