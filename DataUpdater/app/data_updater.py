import json
import Utils
from flask import Flask, jsonify,Response
import time

app = Flask(__name__)

answered = False

@app.route('/')
def index():
    answered = True
    return 'Welcome  to to data-updater!, add /all to download data \
    /TICKER for specific stock'

@app.route('/all')
def download_all_stocks():
    answered = True
    if Utils.GetData.download_all_stocks_snp():
        return 'data-updater - all good'
    else:
        return 'Something went wrong'

@app.route('/update-db')
def download_all_stocks_v2():
    answered = True
    if Utils.GetData.download_all_stocks_snp():
        return "True"
    else:
        return "False"    



@app.route('/progress_test')
def progress_test():
    answered = True
    # def generate_progress():
    #     for i in range(11):  # Assuming progress from 0% to 100% in 10 steps
    #         yield 'progress: ' + str(i*10)
    #         time.sleep(1)  # Simulate progress every 1 second
    return Response(Utils.GetData.download_all_stocks_snp_v2(), mimetype='text/event-stream')

@app.route("/<stock_symbol>")
def download_specific_stock_data(stock_symbol):
    if answered:
        return
    if Utils.GetData.download_stock_data(stock_symbol):
        return "Truee"
    else:
        return "False"



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
