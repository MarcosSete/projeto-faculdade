# Laudo de Qualidade — Gerenciador de Tarefas

## 1. Objetivo
Avaliar a qualidade do sistema Gerenciador de Tarefas, considerando funcionamento, facilidade de utilização, integridade das informações e comportamento diante de diferentes situações de uso.

## 2. Funcionalidades avaliadas
- Cadastro e listagem de tarefas.
- Edição de tarefas existentes.
- Conclusão e exclusão de tarefas.
- Validação do preenchimento obrigatório do título.
- Tratamento de páginas inexistentes por meio de erro 404.

## 3. Resultados da avaliação
Com base nos cenários registrados no documento de atividade:

| Funcionalidade | Resultado registrado |
|---|---|
| Cadastro | Tarefa criada com título e descrição; informações armazenadas no banco |
| Listagem | Exibição da tarefa cadastrada na lista principal |
| Edição | Alteração de título e descrição, com atualização da tela |
| Conclusão | Alteração do status e identificação visual da tarefa concluída |
| Exclusão | Remoção da tarefa da listagem e atualização da página |
| Validação | Tentativa de cadastro sem título; verificação do campo obrigatório |
| Erro 404 | Verificação da resposta ao acessar página inexistente |

Os participantes não relataram falhas nas funcionalidades específicas que avaliaram. Isso não significa que todas as funcionalidades tenham sido testadas por cada participante; as limitações individuais estão descritas em [Testes com usuários](testes_usuarios/README.md).

## 4. Testes com usuários
Foram registrados cinco participantes. Os nomes, datas e observações estão transcritos em [`testes_usuarios/README.md`](testes_usuarios/README.md).

**Observação sobre as datas:** a fonte informa 25/06, 23/06 e 20/06 para três participantes, sem indicar o ano; para os outros dois, informa 18/2026 e 16/2026, sem indicar o mês. Os valores foram preservados e precisam ser confirmados, se necessário.

## 5. Erros identificados e pontos de atenção
Não foram relatados erros confirmados nos cenários executados pelos participantes. Foram considerados os seguintes cuidados para manutenção da qualidade:
1. **Validação de dados:** garantir que tarefas sem título não sejam cadastradas.
2. **Integridade do banco de dados:** garantir que alterações e exclusões sejam persistidas corretamente no SQLite.
3. **Tratamento de erros:** apresentar respostas adequadas quando o usuário acessar páginas inexistentes.
4. **Usabilidade:** manter a interface simples e intuitiva.
5. **Atualização das informações:** garantir que as alterações sejam refletidas na listagem.

## 6. Evidências dos testes
O documento de atividade recomenda coletar:
1. Cadastro de uma nova tarefa.
2. Listagem de tarefas.
3. Tarefa após edição.
4. Tarefa marcada como concluída.
5. Exclusão de uma tarefa.
6. Validação de título obrigatório.
7. Resposta de erro 404.

A pasta [`testes_usuarios/prints/`](testes_usuarios/prints/) está preparada para armazenar as capturas. Nenhuma imagem foi incluída no material recebido.

## 7. Conclusão
O Gerenciador de Tarefas contempla as funcionalidades previstas para o gerenciamento básico de tarefas e utiliza Python/Flask no back-end, HTML/CSS na interface e SQLite para persistência. A organização MVC favorece a manutenção do código, e os testes automatizados com pytest apoiam a verificação dos comportamentos.

Nos relatos fornecidos, os participantes não identificaram falhas nos recursos que testaram. A avaliação final deve considerar também a execução completa dos testes automatizados, a confirmação das datas registradas e a inclusão das evidências visuais recomendadas.
