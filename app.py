from flask import Flask, Response
from prometheus_client import Gauge, generate_latest, CONTENT_TYPE_LATEST
import random

app = Flask(__name__)

accuracy = Gauge("model_accuracy", "Model Accuracy")
precision = Gauge("model_precision", "Model Precision")
recall = Gauge("model_recall", "Model Recall")
f1_score = Gauge("model_f1_score", "Model F1 Score")

@app.route("/")
def home():
    return "Monitoring ML Running"

@app.route("/metrics")
def metrics():

    accuracy.set(random.uniform(0.80, 0.95))
    precision.set(random.uniform(0.80, 0.95))
    recall.set(random.uniform(0.80, 0.95))
    f1_score.set(random.uniform(0.80, 0.95))

    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
