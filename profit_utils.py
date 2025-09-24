import json
import os

# Compute absolute path to datasets folder
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CROP_DATA_FILE = os.path.join(BASE_DIR, "datasets", "crop_data.json")

# Load crop data
with open(CROP_DATA_FILE, "r") as f:
    CROP_DATA = json.load(f)

def get_crop_data(crop, climate):
    try:
        return CROP_DATA[crop][climate]
    except KeyError:
        return None
