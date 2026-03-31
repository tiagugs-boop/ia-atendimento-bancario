# API de Atendimento Bancário com IA

Projeto desenvolvido em Python utilizando Flask e modelos de NLP para simular uma solução de inteligência artificial aplicada ao atendimento bancário.

## Objetivo

Demonstrar uma aplicação prática de IA para:

- Análise de sentimento de mensagens de clientes
- Classificação de demandas (reclamação, dúvida, elogio, transação)
- Geração de resposta automatizada

## Contexto de Negócio

Este projeto simula um cenário comum em instituições financeiras, onde grandes volumes de mensagens de clientes precisam ser analisados e classificados rapidamente.

A solução pode ser aplicada em:

- Triagem automatizada de atendimentos
- Identificação de clientes insatisfeitos
- Priorização de demandas críticas
- Apoio a canais digitais e atendimento automatizado

## Tecnologias utilizadas

- Python
- Flask
- Transformers (Hugging Face)
- NLP (Processamento de Linguagem Natural)

## Como executar o projeto

### 1. Instalar as dependências.

```bash
pip install -r requirements.txt

```
### 2. Rodar o projeto

```bash
python app.py

```
### 3. A API estará disponível em

```bash
http://127.0.0.1:5000/analyze

```
### Exemplo de uso - Requisição:

{
  "text": "Estou com erro no aplicativo e nao consigo fazer Pix"
}

### Resposta

{
  "texto": "Estou com erro no aplicativo e nao consigo fazer Pix",
  "sentimento": {
    "label": "1 star",
    "score": 0.65
  },
  "categoria": "Reclamacao",
  "resposta_sugerida": "Lamentamos o ocorrido. Sua solicitacao sera analisada pela equipe responsavel."
}


## Diferenciais do projeto
Integração de IA com API REST
Simulação de cenário real bancário
Classificação de mensagens com base em regras de negócio
Estrutura simples e extensível

## Autor

Tiago Gomes da Silva