from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "ok", "timestamp": datetime.datetime.utcnow().isoformat()})

@app.route("/billing")
def billing():
    # Simulando processamento
    return jsonify({"customer": "Joao Silva", "invoice": "R$ 129,90"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

