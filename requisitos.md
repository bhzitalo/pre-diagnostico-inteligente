# 🧠 PrInt — Pré-diagnóstico Inteligente

## 📌 Visão Geral

O **PrInt (Pré-diagnóstico Inteligente)** é uma plataforma digital desenvolvida para auxiliar usuários na avaliação inicial de sintomas de saúde.

Seu objetivo é **orientar o usuário sobre a gravidade dos sintomas**, sugerir possíveis caminhos de atendimento e contribuir para a **detecção precoce de problemas**, sem substituir o diagnóstico médico.

O sistema atua como um **assistente de triagem**, promovendo acesso rápido, simples e seguro à informação em saúde.

## 🎯 Problema

Atualmente, muitas pessoas:

- pesquisam sintomas na internet  
- encontram informações confusas ou alarmistas  
- atrasam a busca por atendimento médico  
- ou procuram ajuda desnecessária  

Isso gera:

- agravamento de doenças  
- sobrecarga no sistema de saúde  
- aumento de custos médicos  

Há uma **falta de ferramentas acessíveis, personalizadas e confiáveis** para orientar o paciente.

---

## 💡 Solução

O PrInt propõe:

- um sistema de **triagem inteligente baseado em sintomas**  
- interação via **chat simples e guiado**  
- classificação do nível de urgência  
- orientação de próximos passos  

O sistema **não realiza diagnóstico médico**, mas fornece **orientações baseadas em lógica estruturada**.

---

## 👤 Público-Alvo

- pessoas que sentem sintomas e não sabem como agir  
- usuários que evitam consultas por medo, custo ou falta de tempo  
- pessoas que buscam orientação inicial antes de procurar atendimento  

---

## ⚙️ Funcionalidades do Sistema

### 🔹 Funcionalidades Principais (MVP)

#### 👤 Cadastro e Login
- criação de conta  
- autenticação de usuário  

---

#### 🧾 Perfil do Usuário
- nome  
- idade  
- sexo  
- histórico básico de saúde (opcional)  

---

#### 💬 Chat de Triagem (CORE)
- usuário descreve sintomas  
- sistema faz perguntas adicionais  
- análise baseada em regras  
- retorno com:
  - possíveis causas (genéricas)  
  - nível de urgência  
  - recomendação  

---

#### 🚦 Classificação de Urgência
- 🟢 Baixa (acompanhar sintomas)  
- 🟡 Moderada (procurar atendimento)  
- 🔴 Alta (buscar atendimento imediato)  

---

#### 📊 Histórico
- registro das interações  
- visualização de atendimentos anteriores  

---

#### 📍 Direcionamento
- sugestão de:
  - tipo de especialista  
  - unidade de saúde (futuro)  

---

### 🔹 Funcionalidades Futuras

- integração com APIs de saúde  
- geolocalização (postos próximos)  
- notificações  
- dashboard de saúde  
- integração com dispositivos (wearables)  

---

## 📋 Requisitos Funcionais

O sistema deve:

- permitir cadastro e login de usuários  
- permitir entrada de sintomas  
- realizar perguntas baseadas nas respostas  
- classificar nível de urgência  
- exibir recomendações  
- armazenar histórico  
- permitir consulta de dados anteriores  

---

## 🔒 Requisitos Não Funcionais

- segurança de dados (LGPD)  
- interface simples e acessível  
- tempo de resposta rápido  
- disponibilidade do sistema  
- escalabilidade futura  
- usabilidade (UX amigável)  

---

## 🧠 Regras de Negócio

- o sistema **não substitui diagnóstico médico**  
- todas as respostas devem conter aviso de orientação  
- classificação de risco deve seguir critérios definidos  
- dados do usuário devem ser protegidos  
- o sistema deve priorizar segurança do usuário  

---

## 🔄 Fluxo do Sistema

1. usuário acessa a plataforma  
2. realiza login  
3. inicia chat  
4. informa sintomas  
5. sistema faz perguntas  
6. sistema analisa respostas  
7. sistema classifica urgência  
8. sistema exibe recomendação  
9. dados são armazenados  

---

## 🏗️ Arquitetura do Sistema

### Backend
- responsável pela lógica  
- processamento de sintomas  
- regras de decisão  

### Frontend
- interface do usuário  
- interação com o chat  

### Banco de Dados
- usuários  
- histórico  
- sintomas  

### Camada de Serviço
- análise de sintomas  
- classificação de risco  

---

## 🗄️ Modelo de Dados (Inicial)

### Usuário
- id  
- nome  
- email  
- senha  
- idade  
- sexo  

---

### Atendimento
- id  
- id_usuario  
- data  
- sintomas  
- resultado  
- urgencia  

---

## ⚠️ Considerações Legais

- não fornecer diagnóstico médico  
- incluir termos de uso  
- incluir aviso:  

> ⚠️ Este sistema não substitui um profissional de saúde

- conformidade com LGPD  

---

## 📈 Diferenciais do Projeto

- foco em triagem inteligente  
- acessibilidade  
- simplicidade de uso  
- potencial de impacto social  
- base para evolução com IA real  

---

## 🚀 Tecnologias Sugeridas

- Backend: Python (Flask / FastAPI)  
- Frontend: HTML, CSS, JS  
- Banco: SQLite → PostgreSQL  
- Versionamento: Git/GitHub  

---

## 📊 Escalabilidade

O sistema pode evoluir para:

- IA avançada  
- integração com hospitais  
- telemedicina  
- análise preditiva  

---

## 🧾 Conclusão

O PrInt é uma solução tecnológica que visa melhorar a forma como as pessoas lidam com sintomas de saúde, promovendo **orientação, prevenção e acesso inteligente ao cuidado médico**.

Ele se posiciona como um sistema de triagem acessível, com potencial de impacto social relevante.