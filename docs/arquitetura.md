# 🏗️ Arquitetura do Sistema — PrInt

## 📌 Visão Geral

O sistema será dividido em três camadas principais:

- frontend  
- backend  
- banco de dados  

## 🖥️ Frontend

Responsável por:

- interface do usuário  
- interação com o sistema  
- exibição de resultados  

Tecnologias sugeridas:

- HTML  
- CSS  
- JavaScript  

## ⚙️ Backend

Responsável por:

- lógica do sistema  
- processamento de dados  
- análise de sintomas  
- autenticação  

Tecnologias sugeridas:

- Python (Flask ou FastAPI)  

## 🗄️ Banco de Dados

Responsável por:

- armazenamento de usuários  
- histórico de atendimentos  
- dados de sintomas  

Tecnologias:

- SQLite (inicial)  
- PostgreSQL (escala)  

## 🔄 Fluxo de Comunicação

1. usuário interage com frontend  
2. frontend envia requisição ao backend  
3. backend processa dados  
4. backend consulta banco  
5. backend retorna resposta  
6. frontend exibe resultado  

## 🧩 Estrutura de Pastas (Sugestão)

```bash
backend/
frontend/
database/
docs/