import logging
from flask import Flask, request, jsonify
from transformers import pipeline

# Configuração de Logs - Essencial para monitoramento em produção
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Singleton para o modelo (Carregamento Preguiçoso/Lazy Loading)
class AIService:
    _model = None

    @classmethod
    def get_model(cls):
        if cls._model is None:
            logger.info("Carregando modelo de IA... Isso pode levar alguns segundos.")
            cls._model = pipeline(
                "sentiment-analysis",
                model="nlptown/bert-base-multilingual-uncased-sentiment"
            )
        return cls._model

# Centralização da Lógica de Negócio (Separação de Preocupações)
def classify_intent(text: str) -> str:
    text = text.lower()
    
    # Mapeamento de prioridades para evitar conflitos
    rules = {
        "Reclamação": ["erro", "problema", "falha", "bug", "péssimo", "ruim"],
        "Transação": ["pix", "transferência", "pagamento", "boleto", "ted"],
        "Dúvida": ["como", "dúvida", "ajuda", "suporte", "onde"],
        "Elogio": ["elogio", "bom", "ótimo", "excelente", "parabéns"]
    }

    for category, keywords in rules.items():
        if any(word in text for word in keywords):
            return category
    
    return "Outros"

def get_automated_response(category: str) -> str:
    responses = {
        "Reclamação": "Lamentamos o ocorrido. Registramos sua insatisfação e nossa equipe de qualidade analisará o caso.",
        "Dúvida": "Estamos prontos para ajudar. Como podemos detalhar essa informação para você?",
        "Transação": "Identificamos que sua dúvida é sobre movimentações financeiras. Verifique seu extrato ou o status do processamento.",
        "Elogio": "Ficamos felizes com seu feedback! Isso nos motiva a melhorar sempre."
    }
    return responses.get(category, "Sua mensagem foi recebida e será tratada em breve.")

# Rota com tratamento de erro robusto
@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()
        
        if not data or "text" not in data or not data["text"].strip():
            return jsonify({"status": "error", "message": "O campo 'text' é obrigatório e não pode estar vazio."}), 400

        text = data["text"]
        
        # Chamada do modelo via Singleton
        model = AIService.get_model()
        sentiment_result = model(text)[0]
        
        category = classify_intent(text)
        response_text = get_automated_response(category)

        return jsonify({
            "status": "success",
            "data": {
                "original_text": text,
                "classification": {
                    "intent": category,
                    "sentiment": sentiment_result['label'],
                    "confidence": f"{sentiment_result['score']:.2%}"
                },
                "suggested_response": response_text
            }
        }), 200

    except Exception as e:
        logger.error(f"Erro crítico no processamento: {str(e)}")
        return jsonify({"status": "error", "message": "Erro interno no processamento da solicitação."}), 500

if __name__ == "__main__":
    # Em produção, não usamos app.run(debug=True). Usamos Gunicorn ou Waitress.
    app.run(host='0.0.0.0', port=5000)