from flask import Flask, jsonify, request

app = Flask(__name__)


def assess_potion(ph, clarity):
    """Classify a potion using its pH and visual clarity."""
    ph = float(ph)
    clarity = clarity.strip().lower()

    if not 0 <= ph <= 14:
        raise ValueError("pH must be between 0 and 14")

    if clarity not in {"clear", "cloudy"}:
        raise ValueError("Clarity must be clear or cloudy")

    if 5.5 <= ph <= 7.5 and clarity == "clear":
        return "Approved"

    if 4.0 <= ph <= 9.0:
        return "Review Required"

    return "Rejected"


@app.get("/")
def home():
    return jsonify(
        application="Potion Quality App",
        message="Submit potion quality data to the /assess endpoint",
        version="1.0.0",
    )


@app.get("/health")
def health():
    return jsonify(status="healthy"), 200


@app.post("/assess")
def assess():
    try:
        data = request.get_json()
        result = assess_potion(data["ph"], data["clarity"])

        return jsonify(
            ph=float(data["ph"]),
            clarity=data["clarity"].strip().lower(),
            result=result,
        ), 200

    except (KeyError, TypeError, ValueError) as error:
        return jsonify(error=str(error)), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
