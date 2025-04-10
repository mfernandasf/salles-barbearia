# Requisitos do Sistema de Barbearia

## 1. Introdução

Sistema de gerenciamento para barbearia possui funcionalidades de agendamento, venda de produtos e gestão de barbeiros.

## 2. Requisitos Funcionais

### 2.1 Gestão de Clientes

- Cadastrar, editar, visualizar e excluir clientes
- Manter histórico de serviços realizados
- Cadastro com: nome, telefone, e-mail, data de nascimento

### 2.2 Agendamentos

- Agendar horários com barbeiros específicos
- Visualizar agenda por dia/semana/mês
- Cancelar e reagendar serviços

### 2.3 Produtos

- Cadastrar produtos para venda (pomadas, shampoos, etc.)
- Controlar estoque
- Registrar vendas

### 2.4 Barbeiros

- Cadastrar barbeiros com especialidades
- Definir horários de trabalho
- Visualizar agenda individual

## 3. Requisitos Não Funcionais

- Sistema web responsivo
- Banco de dados PostgreSQL
- Autenticação de usuários
- API Restful com FastAPI
- Contêinerização com Docker
