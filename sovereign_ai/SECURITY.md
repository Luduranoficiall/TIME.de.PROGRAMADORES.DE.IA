# Segurança SOVEREIGN_AI_SYSTEM

- Criptografia AES (Fernet) para campos sensíveis no banco
- Variáveis .env nunca versionadas
- Logs mascarados automaticamente
- Recomendado: rodar sempre sob HTTPS/TLS
- Armazenamento de segredos em vault seguro (ex: AWS Secrets Manager)
- API Keys/JWTs com rotação periódica
- Backups criptografados

## Como usar
- Defina a variável FERNET_KEY no ambiente para garantir chave única
- Use setup_masked_logger() do log_utils.py no entrypoint
- Nunca exponha .env ou chaves em logs ou código
- Para produção, configure HTTPS no proxy reverso (Nginx, Traefik, etc)
