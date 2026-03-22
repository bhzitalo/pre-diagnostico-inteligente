# 🏗️ Diagrama de Arquitetura — PrInt

Este diagrama apresenta a estrutura básica da arquitetura do sistema PrInt, mostrando a comunicação entre usuário, interface, backend, serviço de triagem e banco de dados.

```mermaid
flowchart TD
    A[Usuário] --> B[Frontend]
    B --> C[Backend / API]
    C --> D[Serviço de Triagem]
    C --> E[Banco de Dados]

    D --> C
    E --> C
    C --> B
    B --> A