from flask import Flask
#from config.settings import Config
from api.routes.stock_routes import get_stock
from api.routes.stock_routes import stock_bp
#from api.routes.report_routes import 

def create_app():
    app = Flask(__name__)
    #app.config.from_object(Config)
    
    # Register API routes
    app.register_blueprint(stock_bp, url_prefix="/stocks")
    #app.register_blueprint(report_bp, url_prefix="/reports")
    
    return app
