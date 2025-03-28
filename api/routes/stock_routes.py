from flask import Blueprint, request
from api.controllers.openai.stock_controller import  search_stock, get_top10projections_by_sector

stock_bp = Blueprint('stock_bp', __name__)

# Define routes for the stock API
@stock_bp.route('/<stock_symbol>', methods=['GET'])
def get_stock(stock_symbol):
    print('stock_symbol')
    return search_stock(stock_symbol)
@stock_bp.route('/top10projections', methods=['GET'])
def top10projections():
    sector = request.args.get('sector')
    if not sector:
      return "Sector parameter is required", 400
  
    return get_top10projections_by_sector(sector)
