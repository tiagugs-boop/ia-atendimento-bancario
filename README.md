# 🏦 IA de Atendimento Bancário (NLU Service)

### 📄 Contexto de Negócio
Este projeto é um **MVP (Minimum Viable Product)** de uma API de Inteligência Artificial voltada para a classificação automática de demandas em canais digitais bancários. O objetivo é reduzir o tempo médio de resposta (SLA) e priorizar atendimentos críticos (como falhas em transações PIX) através de Processamento de Linguagem Natural (NLP).

### 🛠️ Tecnologias Utilizadas
* **Python 3.10+**: Linguagem base para processamento de dados.
* **Flask**: Micro-framework para criação de APIs leves e escaláveis.
* **Hugging Face (Transformers)**: Utilização do modelo `BERT multilingual` para análise de sentimentos.
* **Logging & Error Handling**: Práticas de resiliência para ambiente corporativo.

---

### 🏗️ Arquitetura e Decisões Técnicas
Para atender aos padrões de qualidade exigidos em sistemas bancários, o projeto foi estruturado com:

1.  **Singleton Pattern**: O modelo de IA é carregado via *Lazy Loading*, garantindo que a memória RAM seja utilizada de forma eficiente e o modelo carregado apenas uma vez.
2.  **Separação de Preocupações**: A lógica de classificação de intenções é isolada da camada de transporte (API), facilitando a manutenção e a criação de testes unitários.
3.  **Resiliência (Try-Except)**: A API possui tratamento de erros global, evitando que falhas de processamento interrompam o serviço (Status 500 estruturado).
4.  **Validação de Payload**: Implementação de verificações de entrada para garantir a integridade dos dados processados (Status 400).

---

### 🚀 Como Executar o Projeto

#### 1. Clonar o repositório
```bash
git clone [https://github.com/tiagugs-boop/ia-atendimento-bancario.git](https://github.com/seu-usuario/ia-atendimento-bancario.git)
cd ia-atendimento-bancario

```
#### 2. Instalar as dependencias
pip install -r requirements.txt

#### 3. Rodar o servidor
python app.py

### Requisição POST
{
  "text": "Não consigo realizar um PIX, aparece erro de conexão."
}
### Resposta da API
{
  "status": "success",
  "data": {
    "classification": {
      "confidence": "98.45%",
      "intent": "Transação",
      "sentiment": "negative"
    },
    "original_text": "Não consigo realizar um PIX, aparece erro de conexão.",
    "suggested_response": "Identificamos que sua dúvida é sobre movimentações financeiras..."
  }
}