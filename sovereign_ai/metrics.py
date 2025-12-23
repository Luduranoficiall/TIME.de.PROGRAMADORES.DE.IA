from prometheus_client import Counter, Histogram, start_http_server
import time

# Métricas principais
EXECUTIONS_TOTAL = Counter('executions_total', 'Total de execuções', ['tenant', 'agent'])
EXECUTION_SCORE = Histogram('execution_score', 'Score final da execução', ['tenant'])
EXECUTION_TIME = Histogram('execution_time_seconds', 'Tempo de execução', ['tenant', 'agent'])
TOKENS_USED = Counter('tokens_used_total', 'Tokens usados por execução', ['tenant', 'agent'])
COST_USD = Counter('cost_usd_total', 'Custo em USD', ['tenant'])
RETRY_RATE = Counter('retry_rate_total', 'Taxa de retry', ['tenant'])

# Inicializa servidor Prometheus na porta 8001
start_http_server(8001)

def track_execution(tenant, agent, score, exec_time, tokens, cost, retry):
    EXECUTIONS_TOTAL.labels(tenant, agent).inc()
    EXECUTION_SCORE.labels(tenant).observe(score)
    EXECUTION_TIME.labels(tenant, agent).observe(exec_time)
    TOKENS_USED.labels(tenant, agent).inc(tokens)
    COST_USD.labels(tenant).inc(cost)
    if retry:
        RETRY_RATE.labels(tenant).inc()
