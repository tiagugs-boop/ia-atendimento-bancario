from flask import Flask, request, jsonify
from transformers import pipeline

# Inicializa a aplicação Flask
app = Flask(__name__)

# Carrega o modelo de análise de sentimento
sentiment_model = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)

# Função simples de classificação (regra manual)
def classify_text(text):
    text = text.lower()

    if any(word in text for word in ["erro", "problema", "falha", "bug"]):
        return "Reclamação"

    elif any(word in text for word in ["como", "dúvida", "ajuda", "suporte"]):
        return "Dúvida"

    elif any(word in text for word in ["elogio", "bom", "ótimo", "excelente"]):
        return "Elogio"

    elif any(word in text for word in ["pix", "transferência", "pagamento"]):
        return "Transação"

    else:
        return "Outros"

# Gera resposta com base na categoria
def generate_response(category):
    responses = {
        "Reclamação": "Lamentamos o ocorrido. Sua solicitação será analisada pela equipe responsável.",
        "Dúvida": "Estamos aqui para ajudar. Poderia fornecer mais detalhes sobre sua dúvida?",
        "Outros": "Sua mensagem foi recebida e será tratada em breve."
    }
    return responses.get(category, "Mensagem recebida.")
    
# Rota principal da API
@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    # Segurança: caso não venha texto
    if not data or "text" not in data:
        return jsonify({"erro": "Envie um campo 'text' no JSON"}), 400

    text = data["text"]

    # Processamento
    sentiment = sentiment_model(text)[0]
    category = classify_text(text)
    response = generate_response(category)

    # Retorno
    return jsonify({
        "texto": text,
        "sentimento": sentiment,
        "categoria": category,
        "resposta_sugerida": response
    })

# Inicialização do servidor
if __name__ == "__main__":
    app.run(debug=True)