from utils.profit_utils import get_crop_data

class ProfitAnalyzer:
    def __init__(self, acres, crop, climate):
        self.acres = acres
        self.crop = crop
        self.climate = climate
        self.crop_info = get_crop_data(crop, climate)

    def calculate(self):
        if not self.crop_info:
            return {"error": "Crop or climate data not found."}

        yield_base = self.crop_info['yield_per_acre']
        cost_per_acre = self.crop_info['cost_per_acre']
        seasonal_factors = self.crop_info.get("seasonal_factors", {"Default": 1.0})
        price_fluctuation = self.crop_info.get("price_fluctuation", {"Default": self.crop_info['price_per_unit']})

        results = {}
        for season, factor in seasonal_factors.items():
            estimated_yield = yield_base * factor * self.acres
            price = price_fluctuation.get(season, self.crop_info['price_per_unit'])
            revenue = estimated_yield * price
            total_cost = cost_per_acre * self.acres
            profit = revenue - total_cost

            results[season] = {
                "estimated_yield": estimated_yield,
                "revenue": revenue,
                "profit": profit
            }

        return results
