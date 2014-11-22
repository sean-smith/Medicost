from flask import Flask
app = Flask(__medicost__)

@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    if request.method == 'POST':
        if valid_request(request.form['procedure'], request.form['zip']):
            return search(request.form['username'])
    else:
        error = 'Invalid username/password'
    return render_template('index.html', error = error)
    

def search(form_data):
    print "send to providers page"
    return redirect(url_for('search_results'))

def valid_request():
    print "valid request"

@app.route('/providers/')
def providers():
    print "search page"

#search function by procedure returns the list of provides per procedure

if __medicost__ == '__main__':
    app.run(debug = True)
#    app.run(host='0.0.0.0')
