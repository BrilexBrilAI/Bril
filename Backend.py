from flask import Flask, request, jsonify
from riva.client import ASRService, NLPService
import riva.client

# Initialize Flask app
app = Flask(__name__)

# Configure Riva Client
auth = riva.client.Auth(uri="localhost:50051")
asr_service = ASRService(auth)
nlp_service = NLPService(auth)

# Dummy product data
products = [
    {"name": "Apple iPhone 15", "brand": "Apple", "price": "350000"},
    {"name": "Samsung Galaxy S23", "brand": "Samsung", "price": "320000"},
    {"name": "Google Pixel 8", "brand": "Google", "price": "300000"},
    {"name": "OnePlus 11", "brand": "OnePlus", "price": "280000"},
    {"name": "Xiaomi Mi 13", "brand": "Xiaomi", "price": "250000"},
    {"name": "Sony Xperia 1 IV", "brand": "Sony", "price": "310000"},
    {"name": "Oppo Find X5 Pro", "brand": "Oppo", "price": "270000"},
    {"name": "Motorola Edge 30", "brand": "Motorola", "price": "230000"},
    {"name": "Realme GT 2 Pro", "brand": "Realme", "price": "220000"},
    {"name": "Asus ROG Phone 6", "brand": "Asus", "price": "290000"},

    {"name": "Apple MacBook Air (M2)", "brand": "Apple", "price": "420000"},
    {"name": "Dell XPS 13", "brand": "Dell", "price": "390000"},
    {"name": "HP Spectre x360", "brand": "HP", "price": "370000"},
    {"name": "Lenovo ThinkPad X1 Carbon", "brand": "Lenovo", "price": "400000"},
    {"name": "Razer Blade 15", "brand": "Razer", "price": "450000"},
    {"name": "Asus ZenBook 14", "brand": "Asus", "price": "350000"},
    {"name": "Microsoft Surface Laptop 5", "brand": "Microsoft", "price": "410000"},
    {"name": "Acer Predator Helios 300", "brand": "Acer", "price": "380000"},
    {"name": "Samsung Galaxy Book Pro 360", "brand": "Samsung", "price": "360000"},
    {"name": "Gigabyte AORUS 15P", "brand": "Gigabyte", "price": "400000"},

    {"name": "Samsung QN90B Neo QLED 4K TV", "brand": "Samsung", "price": "450000"},
    {"name": "LG OLED C1 Series 4K TV", "brand": "LG", "price": "470000"},
    {"name": "Sony Bravia XR A80J OLED TV", "brand": "Sony", "price": "490000"},
    {"name": "TCL 6-Series R635 4K TV", "brand": "TCL", "price": "350000"},
    {"name": "Vizio M-Series Quantum 4K TV", "brand": "Vizio", "price": "340000"},
    {"name": "Hisense U8H Quantum Series 4K TV", "brand": "Hisense", "price": "330000"},
    {"name": "Philips Ambilight 4K UHD TV", "brand": "Philips", "price": "360000"},
    {"name": "Sharp AQUOS 4K TV", "brand": "Sharp", "price": "310000"},
    {"name": "Sceptre 65-inch 4K Ultra HD LED TV", "brand": "Sceptre", "price": "280000"},
    {"name": "Xiaomi Mi TV Q1 75\"", "brand": "Xiaomi", "price": "300000"},

    {"name": "Apple Watch Series 9", "brand": "Apple", "price": "150000"},
    {"name": "Samsung Galaxy Watch 6", "brand": "Samsung", "price": "130000"},
    {"name": "Garmin Forerunner 945", "brand": "Garmin", "price": "140000"},
    {"name": "Fitbit Charge 5", "brand": "Fitbit", "price": "90000"},
    {"name": "Amazfit GTR 4", "brand": "Amazfit", "price": "85000"},
    {"name": "Huawei Watch GT 3 Pro", "brand": "Huawei", "price": "120000"},
    {"name": "Withings Steel HR Sport", "brand": "Withings", "price": "95000"},
    {"name": "Fossil Gen 6", "brand": "Fossil", "price": "88000"},
    {"name": "Oura Ring Generation 3", "brand": "Oura", "price": "110000"},
    {"name": "Suunto 9 Peak Pro", "brand": "Suunto", "price": "125000"}
]

@app.route("/api/search", methods=["POST"])
def search():
    data = request.get_json()
    query = data.get("query", "").lower()

    # Example: Use NLP service to process query (here we use direct matching)
    matches = [
        product for product in products
        if query in product["name"].lower()
        or query in product["brand"].lower()
        or query in product["price"]
    ]
    return jsonify(matches)

if __name__ == "__main__":
    app.run(debug=True)
