# 🧠 PrInt — Pré-diagnóstico Inteligente

> Sistema de triagem inteligente que analisa sintomas e orienta usuários sobre o nível de urgência e próximos passos em saúde.

---

## 📌 Sobre o Projeto

O **PrInt (Pré-diagnóstico Inteligente)** é uma plataforma desenvolvida com o objetivo de auxiliar usuários na avaliação inicial de sintomas de saúde.

Através de um sistema de triagem inteligente, o usuário recebe orientações sobre a gravidade dos sintomas e possíveis próximos passos, promovendo **detecção precoce** e **melhor tomada de decisão**.

> ⚠️ Este sistema não substitui um profissional de saúde.

---

## 🎯 Problema

Muitas pessoas:

- pesquisam sintomas na internet e recebem informações imprecisas  
- ignoram sinais importantes de saúde  
- atrasam a busca por atendimento médico  
- ou procuram atendimento desnecessário  

Isso gera impacto direto em:

- agravamento de doenças  
- sobrecarga no sistema de saúde  
- aumento de custos  

---

## 💡 Solução

O PrInt propõe:

- 💬 Chat inteligente baseado em sintomas  
- 🧠 Análise estruturada das informações  
- 🚦 Classificação de urgência  
- 📍 Orientação de próximos passos  

---

## ⚙️ Funcionalidades

### 🔹 MVP (Versão Inicial)

- 👤 Cadastro e login de usuários  
- 🧾 Perfil básico do usuário  
- 💬 Chat de triagem (entrada de sintomas)  
- 🚦 Classificação de urgência (baixa, moderada, alta)  
- 📊 Histórico de atendimentos  
- 📍 Sugestão de encaminhamento  

---

### 🔹 Futuro

- 📍 Geolocalização de unidades de saúde  
- 🔔 Notificações  
- 📈 Dashboard de saúde  
- 🤖 Integração com IA avançada  
- ⌚ Integração com dispositivos (wearables)  

---

## 🧠 Como Funciona

1. O usuário acessa a plataforma  
2. Inicia uma conversa com o sistema  
3. Informa seus sintomas  
4. O sistema faz perguntas adicionais  
5. Realiza uma análise baseada em regras  
6. Classifica o nível de urgência  
7. Exibe orientações  
8. Salva o atendimento no histórico  

---

## 🚦 Classificação de Urgência

- 🟢 **Baixa** → acompanhar sintomas  
- 🟡 **Moderada** → procurar atendimento  
- 🔴 **Alta** → buscar atendimento imediato  

---

## 🏗️ Arquitetura

- **Frontend:** Interface do usuário  
- **Backend:** Lógica e processamento  
- **Banco de Dados:** Armazenamento de dados  
- **Serviços:** Análise de sintomas e classificação  

---

## 🗄️ Modelo de Dados (Inicial)

### Usuário
- id  
- nome  
- email  
- senha  
- idade  
- sexo  

### Atendimento
- id  
- id_usuario  
- data  
- sintomas  
- resultado  
- urgencia  

---

## 🔒 Requisitos

### Funcionais
- Cadastro e login  
- Entrada de sintomas  
- Classificação de urgência  
- Exibição de recomendações  
- Armazenamento de histórico  

### Não Funcionais
- Segurança de dados (LGPD)  
- Interface simples e acessível  
- Boa performance  
- Escalabilidade  

---

## ⚠️ Considerações Legais

- O sistema não realiza diagnóstico médico  
- Deve incluir termos de uso  
- Deve respeitar a LGPD  

> ⚠️ Este sistema fornece apenas orientações e não substitui avaliação médica.

---

## 🚀 Tecnologias

- **Backend:** Python (Flask ou FastAPI)  
- **Frontend:** HTML, CSS, JavaScript  
- **Banco de Dados:** SQLite / PostgreSQL  
- **Versionamento:** Git + GitHub  

---

## 📈 Escalabilidade

O projeto pode evoluir para:

- IA avançada  
- integração com hospitais  
- telemedicina  
- análise preditiva  

---

## 👥 Equipe

Projeto desenvolvido por:

- Ítalo  
- Cintia  
- Kauan  
- Stefany  
- Mateus  

---

## 📚 Status do Projeto

🚧 Em desenvolvimento

---

## 📄 Licença

Este projeto é de caráter acadêmico e educacional.

---

## 💬 Contato

Caso tenha interesse em contribuir ou saber mais:

- LinkedIn  
- Email  

---

## ⭐ Contribuição

Sinta-se à vontade para contribuir com melhorias, sugestões ou novas funcionalidades.