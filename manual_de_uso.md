# Manual de Uso — Gerenciador de Tarefas

## O que é
Sistema web para organizar tarefas do dia a dia: cadastrar, editar, concluir e excluir.

## Como acessar
- **Online:** acesse o link da solução em funcionamento (informado no documento de entrega).
- **Local:** siga o passo a passo em [README do código](todo-app/README.md) e abra http://127.0.0.1:5000.

## Tela inicial (lista de tarefas)
Mostra todas as tarefas em uma tabela com título, descrição, vencimento e status (**Pendente** ou **Concluída**). Se não houver tarefas, aparece a mensagem "Nenhuma tarefa cadastrada ainda".

## Como criar uma tarefa
1. Clique em **+ Nova tarefa**.
2. Preencha o **Título** (obrigatório). Descrição e data de vencimento são opcionais.
3. Clique em **Salvar**. A tarefa aparece na lista com a mensagem "Tarefa criada com sucesso!".

Se tentar salvar sem título, o sistema mostra "O título é obrigatório." e não cria a tarefa.

## Como editar
1. Na linha da tarefa, clique em **Editar**.
2. Altere os campos desejados (inclusive o status) e clique em **Salvar**.
3. **Cancelar** volta para a lista sem alterar nada.

## Como concluir / reabrir
Clique em **Concluir** na linha da tarefa. Ela fica riscada e com status "Concluída". Para desfazer, clique em **Reabrir**.

## Como excluir
Clique em **Excluir** e confirme na janela que aparece. A exclusão é definitiva.

## Mensagens do sistema
| Mensagem | Significado |
|---|---|
| Tarefa criada com sucesso! | A tarefa foi salva |
| Tarefa atualizada com sucesso! | As alterações foram salvas |
| Tarefa excluída. | A tarefa foi removida |
| O título é obrigatório. | Preencha o título para salvar |
| Página 404 | O endereço ou a tarefa não existe |
