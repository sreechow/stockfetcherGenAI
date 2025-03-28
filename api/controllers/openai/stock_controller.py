import os
import requests
from openai import OpenAI
from flask import Flask, request, jsonify
from api.utils.savedata import  save_to_json

# Load API Key securely from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
print(OPENAI_API_KEY)
client = OpenAI(api_key="")

def fetch_stock_news(prompt_query):
    """
    Fetch stock market news using OpenAI Web Search
    """
    try:
        #prompt_query = f"What is the revenue growth projection for {stock_symbol} in {market}? for 2025"
        print(prompt_query)
        projection_response = client.responses.create(
            model= "gpt-4o", #"gpt-4o",
            tools=[{
                "type": "web_search_preview",
                "search_context_size": "low",
            }],
            input=prompt_query
        )
        print(projection_response.output_text)
        return jsonify({ "projection": projection_response.output_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def process_report():
    """
    Process uploaded PDF file and extract relevant financial data
    """
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    
    file = request.files['file']
    # Save and process file (can integrate OpenAI File Search here)
    # For now, we return a placeholder response
    return jsonify({"message": "File received, processing logic to be implemented."})

#print(search_stocks())

def get_stock_info(stock_symbol):
    # Here you would typically fetch stock data from a database or external API
    # For this example, let's assume it's a static response.
    print('stock symbol: ', stock_symbol)
    stock_data = {
        "symbol": stock_symbol,
        "price": 150.25,
        "company": "Company XYZ"
    }
    return jsonify(stock_data)

def search_stock(stock_symbol):
    """
    Fetch stock market news using OpenAI Web Search
    """
    #stock_symbol = 'NVDA'
    market ='NASDAQ'  # Default to NASDAQ
        
    if not stock_symbol:
            return jsonify({"error": "Stock symbol is required"}), 400
    query_template  = f"What is the revenue growth projection for {stock_symbol} in {market}? for 2025"
    return fetch_stock_news(query_template)

def get_stock_projection(self, stock_symbol):
        """
        Gets the revenue growth projection for a given stock symbol.

        Args:
            stock_symbol (str): The stock symbol to get the projection for.

        Returns:
            tuple: A tuple containing the JSON response and the HTTP status code.
        """
        query_template = "What is the revenue growth projection for {stock_symbol} in {market}? for 2025"
        return self.search_stock(stock_symbol, query_template)

def get_top10projections_by_sector(sector):
        """
        Gets the top 10 stock projections for a given sector.

        Args:
            sector (str): The sector to search for.

        Returns:
            tuple: A tuple containing the JSON response and the HTTP status code.
        """
        print('get_top10projections_by_sector')
        #print(sector)
        market ='NASDAQ' 
        query_template = f"What are the top 10 stocks with the highest revenue growth projections in the {sector} sector for {market}?"
       
        return fetch_stock_news(query_template)

     
        