from flask import Flask, request, render_template
from firebase import firebase
import pandas as pd
app = Flask(__name__, static_url_path='')

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    error = None
    if request.method == 'GET':
        procedure =  request.args.get('procedure')
        zip_code = request.args.get('zip')
        results = server_call(procedure, zip_code)
        return render_template('results.html', data={"results": results})
    else:
        error = 'invalid request'
        return '500'


def server_call(procedures, zip_code):
    largeframe =  pd.read_csv("CSV_DATA_LOCATION",header=1)
    results = largeframe.loc[(largeframe.nppes_provider_zip == zip_code) & (largeframe.hcpcs_description == procedures), ['nppes_provider_last_org_name', 'nppes_provider_first_name',"average_Medicare_allowed_amt","average_Medicare_payment_amt"]]
    return  results.sort(['average_Medicare_allowed_amt', 'average_Medicare_payment_amt'], ascending=[1, 0])

if __name__ == '__main__':
    app.run(debug = True, port=80)
    #app.run(host='0.0.0.0')
