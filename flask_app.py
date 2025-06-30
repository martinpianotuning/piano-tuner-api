# flask_app.py

from flask import Flask, jsonify, request
import database
import area_data

app = Flask(__name__)

# --- API ENDPOINTS ---

@app.route("/api/customers/all")
def get_all_customers_api():
    try:
        customers = database.get_all_customers()
        return jsonify([dict(c) for c in customers])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/customers/due")
def get_due_customers_api():
    try:
        customers = database.get_due_customers()
        return jsonify([dict(c) for c in customers])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/customers/area_search/<string:city>")
def area_search_api(city):
    try:
        areas = area_data.AREA_MAP.get(city.lower(), [])
        customers = database.search_customers_by_area_and_due_date(areas)
        return jsonify([dict(c) for c in customers])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/customer/<int:customer_id>")
def get_customer_details_api(customer_id):
    try:
        details = database.get_customer_details(customer_id)
        return jsonify(dict(details) if details else None)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/customer/add", methods=['POST'])
def add_customer_api():
    try:
        data = request.get_json()
        new_id = database.add_customer(data)
        return jsonify({"success": True, "new_id": new_id})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/customer/update/<int:customer_id>", methods=['PUT'])
def update_customer_api(customer_id):
    try:
        data = request.get_json()
        database.update_customer(customer_id, data)
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/customer/delete/<int:customer_id>", methods=['DELETE'])
def delete_customer_api(customer_id):
    try:
        database.delete_customer(customer_id)
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500