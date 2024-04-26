import Utils
import ToHtml
from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/as-json')
def return_list_as_json():    
    #return json of stock and it's distance
    return jsonify(Utils.AnalyzeData.analyze_all_stocks()[:150])

@app.route('/as-json/<stock_symbol>')
def index_single_stock_as_json(stock_symbol):    
    distance_from_sma = Utils.AnalyzeData.calculate_distance_from_sma_for_stock(stock_symbol)
    if distance_from_sma == None:
        return [[stock_symbol, "not exists in DB"]]
    return [[stock_symbol, distance_from_sma]]



@app.route('/<stock_symbol>')
def index_single_stock(stock_symbol):
    distance_from_sma = Utils.AnalyzeData.calculate_distance_from_sma_for_stock(stock_symbol)
    if distance_from_sma == None:
        return "STOCK NOT FOUND"
    return ToHtml.Html.touple_to_html_table([(stock_symbol, distance_from_sma)])

@app.route('/')
def index():
    sorted_stocks = Utils.AnalyzeData.analyze_all_stocks()[:20] 
    # Create an HTML string with a basic table structure and some minimal styling
    return ToHtml.Html.touple_to_html_table(sorted_stocks)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
