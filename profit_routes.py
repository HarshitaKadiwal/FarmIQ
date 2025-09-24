from flask import Blueprint, request, jsonify
from models.profit_model import ProfitAnalyzer

profit_bp = Blueprint('profit', __name__)

@profit_bp.route('/calculate_profit', methods=['POST'])
def calculate_profit():
    data = request.json
    acres = data.get("acres")
    crop = data.get("crop")
    climate = data.get("climate")

    if not all([acres, crop, climate]):
        return jsonify({"error": "Missing fields"}), 400

    analyzer = ProfitAnalyzer(float(acres), crop, climate)
    result = analyzer.calculate()
    return jsonify(result)
