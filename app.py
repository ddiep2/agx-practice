from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/api/weather")
def weather():
    params = {
        "latitude": 32.22, "longitude": -110.97,
        "daily": "temperature_2m_max,precipitation_sum,et0_fao_evapotranspiration",
        "timezone": "America/Phoenix", "forecast_days": 3,
    }
    r = requests.get("https://api.open-meteo.com/v1/forecast", params=params, timeout=10)
    return jsonify(r.json()["daily"])

if __name__ == "__main__":
    app.run(debug=True)