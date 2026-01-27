from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("accident_model.pkl")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        data = {
            "road_type": request.form["road_type"],
            "num_lanes": int(request.form["num_lanes"]),
            "curvature": float(request.form["curvature"]),
            "lighting": request.form["lighting"],
            "weather": request.form["weather"],
            "road_signs_present": bool(int(request.form.get("road_signs_present", 0))),
            "public_road": bool(int(request.form.get("public_road", 0))),
            "time_of_day": request.form["time_of_day"],
            "holiday": bool(int(request.form.get("holiday", 0))),
            "school_season": bool(int(request.form.get("school_season", 0))),
            "high_speed": bool(int(request.form.get("high_speed", 0)))
        }

        df = pd.DataFrame([data])
        print(df.iloc[0])
        prediction = round(model.predict(df)[0], 4)

    return render_template("predict.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
