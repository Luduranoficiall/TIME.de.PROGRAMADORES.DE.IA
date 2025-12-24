# Copilot Instructions for AI Coding Agents

## Visão Geral

Esta plataforma orquestra times de programadores de IA em um ambiente multi-tenant, SaaS, com governança, observabilidade, billing, integração GitHub e IA-CTO. O sistema é modular, escalável e segue princípios de clean architecture.

## Arquitetura e Componentes
- **Agentes Especializados**: Localizados em `ia_team_platform/app/agents/` (ex: `architect.py`, `backend.py`, `reviewer.py`, `security.py`). Cada agente executa uma etapa do pipeline de desenvolvimento.
- **Orquestrador**: `orchestrator.py` coordena a pipeline dos agentes.
- **Memória e RAG**: Memória de curto/longo prazo, embeddings e RAG em `memory/` e `rag/`.
- **Core/LLM**: Lógica central, configuração, segurança e integração LLM em `core/` e `infra/`.
- **Domínio e Aplicação**: Modelos de domínio em `domain/`, casos de uso em `application/`.
- **APIs**: Rotas, autenticação e dependências em `api/`.
- **Infraestrutura**: Banco de dados, Redis, rastreamento de custos em `infra/`.
- **Soberania**: Módulos de autoridade, consciência, limites e shutdown em `sovereign/`.

## Workflows Essenciais
- **Build/Run**: Use `docker-compose up --build` em `ia_team_platform/` para subir o ambiente completo.
- **Testes**: (Adicionar instruções específicas se existirem scripts ou comandos de teste.)
- **Debug**: Utilize logs em `core/logging.py` e monitore métricas em `monitoring.py`.

## Convenções e Padrões
- **Pipeline de agentes**: O fluxo é orquestrado pelo `orchestrator`, passando por agentes especializados.
- **Multi-tenant**: Cada tenant é modelado em `domain/tenant.py` e `schemas/tenant.py`.
- **Memória vetorial/RAG**: Use `memory/` e `rag/` para persistência e recuperação de contexto.
- **Integração LLM**: Configurada em `infra/llm.py` e `core/config.py`.
- **Segurança**: Autenticação e autorização em `core/security.py` e `api/auth.py`.

## Integrações e Dependências
- **Banco de Dados**: PostgreSQL + pgvector (ver `docker-compose.yml` e `infra/database.py`).
- **Redis**: Para cache e filas (ver `infra/redis.py`).
- **Stripe**: Billing (ver referências em `core/` e `infra/`).
- **GitHub**: Integração para PRs automáticos (ver `infra/cost_tracker.py` e `github.py`).

## Exemplos e Templates
- Veja `integracoes_exemplos/` para exemplos de integração e templates.

## Dicas para Agentes
- Sempre siga o fluxo de orquestração de agentes.
- Respeite a separação de responsabilidades entre domínio, aplicação, infraestrutura e API.
- Prefira reutilizar componentes existentes.
- Consulte os arquivos README.md para detalhes de uso e arquitetura.

---
Seções incompletas ou dúvidas? Peça feedback para aprimorar estas instruções.