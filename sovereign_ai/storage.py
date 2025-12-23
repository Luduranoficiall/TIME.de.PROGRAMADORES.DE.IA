import os
import psycopg2
import redis

POSTGRES_URL = os.getenv("POSTGRES_URL", "postgresql://user:pass@localhost:5432/sovereign")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

# PostgreSQL Connection
pg_conn = psycopg2.connect(POSTGRES_URL)
pg_conn.autocommit = True

# Redis Connection
redis_client = redis.Redis.from_url(REDIS_URL)

# --- MODELS ---

def create_tables():
    with pg_conn.cursor() as cur:
        cur.execute('''
        CREATE TABLE IF NOT EXISTS tenants (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            plan TEXT NOT NULL,
            status TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT NOW()
        );
        CREATE TABLE IF NOT EXISTS executions (
            id SERIAL PRIMARY KEY,
            tenant_id INTEGER REFERENCES tenants(id),
            intent TEXT,
            output TEXT,
            score INTEGER,
            cost INTEGER,
            created_at TIMESTAMP DEFAULT NOW()
        );
        CREATE TABLE IF NOT EXISTS agent_runs (
            id SERIAL PRIMARY KEY,
            execution_id INTEGER REFERENCES executions(id),
            agent_name TEXT,
            input TEXT,
            output TEXT,
            created_at TIMESTAMP DEFAULT NOW()
        );
        CREATE TABLE IF NOT EXISTS memory_vectors (
            id SERIAL PRIMARY KEY,
            tenant_id INTEGER REFERENCES tenants(id),
            embedding VECTOR(1536),
            content TEXT,
            created_at TIMESTAMP DEFAULT NOW()
        );
        CREATE TABLE IF NOT EXISTS audit_logs (
            id SERIAL PRIMARY KEY,
            tenant_id INTEGER REFERENCES tenants(id),
            action TEXT,
            actor TEXT,
            details TEXT,
            created_at TIMESTAMP DEFAULT NOW()
        );
        ''')

# --- REDIS USAGE EXAMPLES ---
def cache_set(key, value, ex=3600):
    redis_client.set(key, value, ex=ex)

def cache_get(key):
    return redis_client.get(key)
