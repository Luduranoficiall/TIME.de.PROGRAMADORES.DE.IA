# TIME.de.PROGRAMADORES.DE.IA

[![Build Status](https://img.shields.io/github/workflow/status/Luduranoficiall/TIME.de.PROGRAMADORES.DE.IA/CI)](https://github.com/Luduranoficiall/TIME.de.PROGRAMADORES.DE.IA/actions)
[![License](https://img.shields.io/github/license/Luduranoficiall/TIME.de.PROGRAMADORES.DE.IA)](LICENSE)
[![Docker](https://img.shields.io/badge/docker-ready-blue)](https://hub.docker.com/)

## Sumário
- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Arquitetura](#arquitetura)
- [Setup e Execução](#setup-e-execução)
- [APIs e Exemplos de Uso](#apis-e-exemplos-de-uso)
- [Segurança e Governança](#segurança-e-governança)
- [Avançado](#avançado)
- [Contribuição](#contribuição)

---

## Visão Geral
Plataforma IA-First para orquestração de times de programadores de IA, multi-tenant, SaaS, com governança, observabilidade, billing, integração GitHub e IA-CTO para governança de humanos + IA.

## Funcionalidades
- Multi-tenant real
- SaaS: Auth, Billing, Limites, Planos
- Observabilidade: Métricas, Tracing, Custos
- Governança: Políticas, Auditoria, Chaves rotativas
- GitHub Integration: PR automático, branch, review IA
- IA-CTO: Governança de times humanos + IA
- Pronto para produção: PostgreSQL + pgvector, Redis, Stripe-ready, API Key/JWT

## Arquitetura
```
+-------------------+
|    Usuário/API    |
+-------------------+
          |
          v
+-------------------+
|    Orchestrator   | <--- Pipeline de agentes (Architect, Backend, Reviewer, Security)
+-------------------+
          |
          v
+-------------------+
|     Core/LLM      | <--- Memória (curto/longo prazo), RAG, Vetores
+-------------------+
          |
          v
+-------------------+
| Infra/DB/Redis/   |
| Stripe/GitHub     |
+-------------------+
```
- Modular, escalável, clean architecture
- Agentes especializados e pipeline customizável
- Memória vetorial, embeddings, RAG
- Integração LLM (OpenAI, etc)

## Setup e Execução
### Requisitos
- Docker e Docker Compose
- Python 3.12+ (opcional para dev)
- Chaves de API (OpenAI, Stripe, etc)

### Instalação
```bash
git clone https://github.com/Luduranoficiall/TIME.de.PROGRAMADORES.DE.IA.git
cd TIME.de.PROGRAMADORES.DE.IA/sovereign_ai
cp .env.example .env # configure suas chaves
```

### Execução
```bash
docker-compose up --build
```
Acesse a API em http://localhost:8000/execute

## APIs e Exemplos de Uso
### Healthcheck
```http
GET /health
```

### Execução de pipeline
```http
POST /v1/execute
Headers: x-tenant-id: TENANT_ID
Body: { "requirement": "Criar API REST para cadastro de usuários" }
```

### God Mode (admin)
```http
POST /v3/god/execute
Body: { "intent": "Automatize deploy CI/CD", "root_key": "SUA_ROOT_KEY" }
```

### Exemplo de resposta
```json
{
  "final_output": "Código backend seguro criado.",
  "trace": [
    { "agent": "Architect", "output": "Design..." },
    { "agent": "Backend Engineer", "output": "Implement..." },
    { "agent": "Reviewer", "output": "Review..." },
    { "agent": "Security Auditor", "output": "Audit..." }
  ]
}
```

## Segurança e Governança
- Criptografia AES (Fernet) para campos sensíveis
- Variáveis .env nunca versionadas
- Logs mascarados automaticamente
- API Keys/JWTs com rotação periódica
- Auditoria e políticas customizáveis
- Rate limit por tenant
- Recomenda-se HTTPS/TLS em produção

## Avançado
- Observabilidade: Métricas, tracing, custos
- Governança: Auditoria, políticas, rotação de chaves
- GitHub Integration: PR automático, branch, review IA
- LLMs: OpenAI GPT-4o, embeddings, RAG
- Multi-tenant: isolamento total de dados
- Pronto para escalar: PostgreSQL + pgvector, Redis, Stripe

## Contribuição
Pull requests são bem-vindos! Para grandes mudanças, abra uma issue primeiro.

---

> "A IA que orquestra engenheiros, código e negócio, com governança e automação de ponta a ponta."

---

[Documentação avançada](sovereign_ai/DOCUMENTACAO.md) | [Segurança](sovereign_ai/SECURITY.md)

---

## Tópicos Avançados

### Exemplo Avançado: Fluxo Completo de Agentes

**Input:**
```json
{
  "requirement": "Criar API REST para cadastro de usuários com autenticação JWT e validação de e-mail."
}
```
**Output:**
```json
{
  "final_output": "API REST criada com endpoints seguros, autenticação JWT e validação de e-mail.",
  "trace": [
    { "agent": "Architect", "output": "Desenhou arquitetura modular, endpoints, fluxos de autenticação e validação." },
    { "agent": "Backend Engineer", "output": "Implementou endpoints, integração JWT, lógica de validação de e-mail." },
    { "agent": "Reviewer", "output": "Revisou código, sugeriu melhorias de performance e clareza." },
    { "agent": "Security Auditor", "output": "Auditou código, corrigiu possíveis falhas de segurança e sugeriu boas práticas." }
  ]
}
```

### Diagrama de Sequência (Execução de Pipeline)
```
Usuário/API
   |
   | POST /v1/execute
   v
Orchestrator
   |---> ArchitectAgent: design()
   |---> BackendAgent: implement()
   |---> ReviewerAgent: review()
   |---> SecurityAgent: audit()
   v
Resposta final (trace + output)
```

---

## Como Criar Novos Agentes e Pipelines
1. Crie uma nova classe herdando de `BaseAgent`.
2. Implemente o método `run()` ou métodos customizados.
3. Adicione o novo agente ao pipeline no Orchestrator.
4. (Opcional) Crie pipelines customizados para fluxos específicos.

Exemplo:
```python
from app.agents.base import BaseAgent
class DataScienceAgent(BaseAgent):
    name = "Data Scientist"
    role = "ML Specialist"
    def analyze(self, data: str) -> str:
        return self.run(f"Analyze dataset: {data}")
```

---

## Casos de Uso Reais e Automação
- Onboarding automatizado de times de IA.
- Execução de projetos complexos com múltiplos agentes.
- Governança de código, auditoria e compliance automatizados.
- Orquestração de deploys, integrações e monitoramento.
- Automação de fluxos de CI/CD e revisão de código.

---

## Dicas de Segurança para Produção
- Use HTTPS/TLS sempre (proxy reverso: Nginx, Traefik).
- Armazene segredos em vault seguro (AWS Secrets, GCP Secret Manager, Azure Key Vault).
- Faça rotação periódica de chaves e tokens.
- Ative logs mascarados e monitore acessos.
- Realize backups criptografados e testes de restauração.
- Implemente rate limit e monitore tentativas suspeitas.

---

## Instruções de Deploy em Nuvem
### AWS ECS/Fargate
- Crie um cluster ECS, configure task definition com Docker image.
- Use RDS para PostgreSQL, ElastiCache para Redis.
- Armazene segredos no AWS Secrets Manager.

### GCP Cloud Run
- Deploy direto do Docker, configure Cloud SQL e Memorystore.
- Use Secret Manager para variáveis sensíveis.

### Azure Container Apps
- Deploy container, configure Azure Database for PostgreSQL e Azure Cache for Redis.
- Use Azure Key Vault para segredos.

---

Essas seções avançadas complementam a documentação, tornando o projeto pronto para escala, automação e segurança de nível enterprise. Se quiser mais exemplos, fluxos ou integrações, só avisar!