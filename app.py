from flask import Flask, request, jsonify

def create_app():
    app = Flask(__name__)

    # In-memory store (simple for assignment). Swap to SQLite later if needed.
    app.config["WORKOUTS"] = []

    @app.get("/")
    def health():
        return jsonify({"status": "ok", "service": "ACEest Fitness API"}), 200

    @app.post("/add_workout")
    def add_workout():
        data = request.get_json(silent=True) or {}
        workout = (data.get("workout") or "").strip()
        duration = data.get("duration")

        errors = []
        if not workout:
            errors.append("workout is required")
        if len(workout) > 100:
            errors.append("workout must be <= 100 chars")
        try:
            duration = int(duration)
            if duration <= 0:
                errors.append("duration must be a positive integer")
        except (TypeError, ValueError):
            errors.append("duration must be an integer")

        if errors:
            return jsonify({"ok": False, "errors": errors}), 400

        entry = {"workout": workout, "duration": duration}
        app.config["WORKOUTS"].append(entry)
        return jsonify({"ok": True, "message": "Workout added", "data": entry}), 201

    @app.get("/workouts")
    def list_workouts():
        return jsonify({"count": len(app.config["WORKOUTS"]),
                        "items": app.config["WORKOUTS"]}), 200

    return app

if __name__ == "__main__":
    app = create_app()
    # Bind 0.0.0.0 for Docker; default port 5000
    app.run(host="0.0.0.0", port=5000)
