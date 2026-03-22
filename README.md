# 🧠 PrInt — Pré-diagnóstico Inteligente

> Sistema de triagem inteligente que analisa sintomas e orienta usuários sobre o nível de urgência e próximos passos em saúde.

## 📌 Sobre o projeto

O **PrInt (Pré-diagnóstico Inteligente)** é um projeto acadêmico desenvolvido com o objetivo de criar uma plataforma digital capaz de auxiliar usuários na avaliação inicial de sintomas de saúde.

A proposta do sistema é oferecer uma **triagem inteligente**, ajudando o usuário a entender a gravidade dos sintomas e indicando possíveis próximos passos, de forma simples, rápida e acessível.

> ⚠️ Este sistema **não substitui diagnóstico médico** nem avaliação profissional de saúde.

## 🎯 Objetivo

Desenvolver uma aplicação capaz de:

- coletar sintomas informados pelo usuário
- realizar uma triagem inicial baseada em regras
- classificar o nível de urgência
- orientar o usuário sobre o que fazer a seguir
- armazenar o histórico de atendimentos

## 💡 Problema que o projeto busca resolver

Muitas pessoas pesquisam sintomas na internet e encontram informações confusas, alarmistas ou imprecisas. Isso pode causar:

- atrasos na busca por atendimento médico
- automedicação
- preocupação excessiva
- agravamento de quadros de saúde

O PrInt surge como uma proposta de apoio inicial, oferecendo uma orientação mais estruturada ao usuário.

## ⚙️ Principais funcionalidades

- cadastro e login de usuários
- perfil básico do usuário
- chat de triagem
- análise inicial de sintomas
- classificação de urgência
- recomendação de próximos passos
- histórico de atendimentos

## 🚦 Classificação de urgência

O sistema poderá classificar os sintomas em três níveis:

- 🟢 **Baixa** — acompanhar sintomas
- 🟡 **Moderada** — procurar atendimento
- 🔴 **Alta** — buscar atendimento imediato

## 🏗️ Estrutura do projeto

```text
pre-diagnostico-inteligente/
├── README.md
├── docs/
│   ├── documentacao.md
│   ├── requisitos.md
│   ├── regras-de-negocio.md
│   ├── casos-de-uso.md
│   ├── arquitetura.md
│   ├── diagrama-casos-de-uso.md
│   ├── diagrama-arquitetura.md
│   ├── diagrama-er.md
│   └── diagrama-fluxo.md
├── backend/
├── frontend/
└── database/