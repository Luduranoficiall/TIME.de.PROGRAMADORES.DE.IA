CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE memory_vectors (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id TEXT,
    content TEXT,
    embedding VECTOR(1536),
    created_at TIMESTAMP DEFAULT now()
);

CREATE INDEX ON memory_vectors
USING ivfflat (embedding vector_cosine_ops);
