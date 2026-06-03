from flask import Flask
from prometheus_client import Gauge, generate_latest
import random

app = Flask(__name__)

accuracy = Gauge(
    "model_accuracy",
    "Model Accuracy"
)

precision = Gauge(
    "model_precision",
    "Model Precision"
)

recall = Gauge(
    "model_recall",
    "Model Recall"
)

f1_score = Gauge(
    "model_f1_score",
    "Model F1 Score"
)

@app.route("/")
def home():

    accuracy.set(random.uniform(0.80, 0.95))
    precision.set(random.uniform(0.80, 0.95))
    recall.set(random.uniform(0.80, 0.95))
    f1_score.set(random.uniform(0.80, 0.95))

    return "Monitoring ML Running"

@app.route("/metrics")
def metrics():

    return generate_latest()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
