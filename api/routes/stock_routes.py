from flask import Blueprint, request
from api.controllers.openai.stock_controller import  search_stock, get_top10projections_by_sector
from api.controllers.openai.upload_vector_controller import create_vector_store

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

@stock_bp.route('/create_vector_store', methods=['post'])
def create_vector_store(filepath):
    file_path = request.args.get('file_path')
    if not file_path:
      return "file_path parameter is required", 400
    
    return create_vector_store(file_path)
