# Documentação SOVEREIGN_AI_SYSTEM

## Endpoints principais
- POST /execute
- GET /health

## Onboarding
- register_tenant(tenant_id, plan)
- activate_tenant(tenant_id)
- welcome(tenant_id)

## Segurança
- JWT obrigatório
- HTTPS recomendado
- Campos sensíveis criptografados

## Deploy
- docker-compose.prod.yml
- CI_CD_PIPELINE.yml

## Observabilidade
- Métricas: metrics.py
- Tracing: tracing.py
- Custos: costs.py

## Governança
- Auditoria: governance.py
- Políticas: policies.py
- Rotação de chaves: key_rotation.py

## GitHub Integration
- PR automático: github.py

## Suporte
- [seu-email@dominio.com]
