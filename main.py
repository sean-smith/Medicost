from flask import Flask
app = Flask(__medicost__, static_url_path='')

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    error = None
    if request.method == 'POST':
        print request.form['procedure'], request.form['zip']
    else:
        error = 'Invalid username/password'
    
'''
def search():
    print "send to providers page"
    # assuming return values are in an array
    for each prov in form_data:
        print prov
    return redirect(url_for('search_results'))


def valid_request():
    print "valid request"

@app.route('/providers/')
def providers():
    print "search page"
'''
#search function by procedure returns the list of provides per procedure

if __medicost__ == '__main__':
    app.run(debug = True)
#    app.run(host='0.0.0.0')
