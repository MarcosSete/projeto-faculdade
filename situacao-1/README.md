# Situação 1 — Atualizar o plano de projeto

Revisão do planejamento do projeto (melhoria contínua / KaiZen).

## Escopo
Sistema web de gerenciamento de tarefas com as operações de cadastro, listagem, edição, conclusão e exclusão, com validação do título obrigatório.

## Modelagem (UML)
- [Diagrama de classes](../todo-app/docs/diagrama_de_classes.md)

## Banco de dados
- [DER](../todo-app/docs/DER.md)
- [Dicionário de dados](../todo-app/docs/dicionario_de_dados.md)
- [Projeto físico (schema.sql)](../todo-app/docs/schema.sql) — SGBD: SQLite

## Interface (IHC)
As telas implementadas seguem os princípios do material teórico: interface simples, consistente, com feedback ao usuário (mensagens de sucesso e erro) e ações reversíveis (Reabrir tarefa; confirmação antes de excluir). Veja o [manual de uso](../manual_de_uso.md).

## Melhorias identificadas (a fazer / limitações conhecidas)
- Validar o formato da data também no servidor.
- Limitar o tamanho dos campos no servidor.
- Não há login por usuário (todos veem as mesmas tarefas).
- Não há busca nem filtro por status.
