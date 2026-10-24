from flask import Flask, jsonify

app = Flask(__name__)
counters = {}


@app.get("/")
def index():
    return jsonify({"service": "counter-service", "status": "ok"})


@app.get("/health")
def health():
    return jsonify({"status": "healthy"})


@app.get("/counters")
def list_counters():
    return jsonify(counters)


@app.post("/counters/<name>")
def create_counter(name):
    if not name.strip():
        return jsonify({"error": "counter name is required"}), 400
    counters.setdefault(name, 0)
    return jsonify({"name": name, "value": counters[name]}), 201


@app.get("/counters/<name>")
def get_counter(name):
    if name not in counters:
        return jsonify({"error": "counter not found"}), 404
    return jsonify({"name": name, "value": counters[name]})


@app.put("/counters/<name>")
def increment_counter(name):
    if name not in counters:
        return jsonify({"error": "counter not found"}), 404
    counters[name] += 1
    return jsonify({"name": name, "value": counters[name]})


@app.delete("/counters/<name>")
def delete_counter(name):
    if name not in counters:
        return jsonify({"error": "counter not found"}), 404
    del counters[name]
    return jsonify({"deleted": name})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(__import__("os").environ.get("PORT", "8080")))
