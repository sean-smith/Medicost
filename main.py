from flask import Flask, request, render_template
app = Flask(__name__, static_url_path='')


procedures = []
def make_list():
    f = open('uniques', 'r')
    global procedures 
    procedures = f.read().split("\n")
    f.close()

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    error = None
    if request.method == 'POST':
        procedure =  request.form['procedure']
        zip_code = request.form['zip']
        make_list()
        print procedures
        return render_template('results.html', data={"provider": message})
        return '200'
    else:
        error = 'invalid request'
        return '500'

    return redirect(url_for('search_results'))

'''
def valid_request():
    print "valid request"

@app.route('/providers/')
def providers():
    print "search page"
'''
#search function by procedure returns the list of provides per procedure

if __name__ == '__main__':
    app.run(debug = True, port=80)
    #app.run(host='0.0.0.0')
