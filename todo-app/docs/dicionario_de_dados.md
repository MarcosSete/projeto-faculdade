# Dicionário de Dados

**Tabela:** `tarefa`
**SGBD:** SQLite (leve, gratuito e amplamente utilizado no mercado)

| Campo | Tipo (SQLite) | Tamanho | Nulo? | Chave | Domínio / Regra | Descrição |
|---|---|---|---|---|---|---|
| id | INTEGER | - | Não | PK (auto incremento) | Inteiro positivo, único | Identificador da tarefa |
| titulo | VARCHAR | 120 | Não | - | Texto livre, não vazio | Título curto da tarefa |
| descricao | VARCHAR | 500 | Sim | - | Texto livre | Detalhamento opcional |
| status | VARCHAR | 20 | Não | - | "Pendente" ou "Concluída" (default: "Pendente") | Situação atual da tarefa |
| data_criacao | DATETIME | - | Não | - | Preenchida automaticamente pelo sistema | Data/hora em que a tarefa foi criada |
| data_vencimento | DATE | - | Sim | - | Data válida (AAAA-MM-DD) | Prazo definido pelo usuário |

## Regras de integridade

- Toda tarefa precisa ter um `titulo` (validado tanto no front-end quanto no back-end).
- `status` só aceita dois valores possíveis, controlados pela aplicação (Controller).
- `id` é gerado automaticamente pelo SGBD, garantindo unicidade.
