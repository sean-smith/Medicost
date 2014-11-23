from flask import Flask, request, render_template
from firebase import firebase
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
    return 2

if __name__ == '__main__':
    app.run(debug = True, port=80)
    #app.run(host='0.0.0.0')
