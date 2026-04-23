# app.py - Flask Web Server

from flask import Flask, jsonify, request, render_template
from operations import (
    add_expense,
    get_all_expenses,
    update_expense,
    delete_expense,
    get_monthly_total,
    get_category_total,
    get_monthly_summary_view,
    get_categories
)

app = Flask(__name__)


# ── Serve frontend ─────────────────────────────
@app.route('/')
def index():
    return render_template('index.html')


# ── Get all expenses ───────────────────────────
@app.route('/api/expenses', methods=['GET'])
def api_get_expenses():
    return jsonify(get_all_expenses())


# ── Add expense ────────────────────────────────
@app.route('/api/expenses', methods=['POST'])
def api_add_expense():
    data = request.json
    add_expense(data['date'], data['name'], data['amount'], data['category_id'])
    return jsonify({'success': True})


# ── Update expense ─────────────────────────────
@app.route('/api/expenses/<int:expense_id>', methods=['PUT'])
def api_update_expense(expense_id):
    data = request.json
    success = update_expense(expense_id, data['amount'])
    return jsonify({'success': success})


# ── Delete expense ─────────────────────────────
@app.route('/api/expenses/<int:expense_id>', methods=['DELETE'])
def api_delete_expense(expense_id):
    success = delete_expense(expense_id)
    return jsonify({'success': success})


# ── Monthly total ──────────────────────────────
@app.route('/api/monthly-total', methods=['GET'])
def api_monthly_total():
    return jsonify(get_monthly_total())


# ── Category total ─────────────────────────────
@app.route('/api/category-total', methods=['GET'])
def api_category_total():
    return jsonify(get_category_total())


# ── Monthly summary view ───────────────────────
@app.route('/api/monthly-summary', methods=['GET'])
def api_monthly_summary():
    return jsonify(get_monthly_summary_view())


# ── Get categories ─────────────────────────────
@app.route('/api/categories', methods=['GET'])
def api_categories():
    return jsonify(get_categories())


if __name__ == '__main__':
    app.run(debug=True)