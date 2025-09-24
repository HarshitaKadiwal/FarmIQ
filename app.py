from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__, template_folder="../frontend")
CORS(app)

@app.route("/profit")
def profit_page():
    return render_template("profit.html")

@app.route("/calculate_profit", methods=["POST"])
def calculate_profit():
    data = request.get_json()
    acres = float(data.get("acres", 0))
    crop = data.get("crop", "Wheat")
    climate = data.get("climate", "Temperate")

    # Example values (you can replace with your own formulas / database)
    crop_data = {
        "Wheat": {"yield_per_acre": 30, "price_per_unit": 210},
        "Rice": {"yield_per_acre": 25, "price_per_unit": 180},
        "Corn": {"yield_per_acre": 40, "price_per_unit": 150},
    }

    # Seasonal factors (Spring, Summer, Winter)
    season_factors = {
        "Spring": 0.8,
        "Summer": 0.5,
        "Winter": 1.0,
    }

    results = []
    if crop in crop_data:
        yield_per_acre = crop_data[crop]["yield_per_acre"]
        price = crop_data[crop]["price_per_unit"]
        base_yield = acres * yield_per_acre

        for season, factor in season_factors.items():
            estimated_yield = int(base_yield * factor)
            revenue = estimated_yield * price
            cost = estimated_yield * 60   # assume fixed cost/unit
            profit = revenue - cost

            results.append({
                "season": season,
                "yield": estimated_yield,
                "revenue": revenue,
                "profit": profit
            })

    return jsonify({"success": True, "results": results})

if __name__ == "__main__":
    app.run(debug=True)
