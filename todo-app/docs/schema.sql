-- Projeto físico do banco de dados
-- SGBD: SQLite
-- Esta tabela é criada automaticamente pela aplicação (SQLAlchemy),
-- mas o script abaixo documenta a estrutura física equivalente.

CREATE TABLE IF NOT EXISTS tarefa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(120) NOT NULL,
    descricao VARCHAR(500),
    status VARCHAR(20) NOT NULL DEFAULT 'Pendente',
    data_criacao DATETIME NOT NULL,
    data_vencimento DATE
);
