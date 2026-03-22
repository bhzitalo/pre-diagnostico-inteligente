# 🎭 Diagrama de Casos de Uso — PrInt

Este diagrama representa as principais interações do usuário com o sistema PrInt.

```mermaid
flowchart LR
    U[Usuário]

    UC1((Cadastrar conta))
    UC2((Fazer login))
    UC3((Editar perfil))
    UC4((Informar sintomas))
    UC5((Responder perguntas adicionais))
    UC6((Receber classificação de urgência))
    UC7((Visualizar recomendação))
    UC8((Consultar histórico))
    UC9((Encerrar sessão))

    U --> UC1
    U --> UC2
    U --> UC3
    U --> UC4
    U --> UC5
    U --> UC6
    U --> UC7
    U --> UC8
    U --> UC9