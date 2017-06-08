from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key= 'ThisIsSecret'

@app.route('/')

def index():
  session["mynum"] = random.randint(1, 100)  
  print session['mynum']
  return render_template("index.html")

@app.route('/guess', methods=['post'])
def guess():
    print request.form['guess']
    print session['mynum']
    # guessnum = request.form['guess']
    if int(request.form['guess']) < session['mynum']:
        return redirect ('/toolow')
    elif int(request.form['guess']) > session['mynum']:
        print "toohigh"
        return redirect('/toohigh')
    elif int(request.form['guess']) == session['mynum']:
        return redirect('/success')

@app.route('/toolow')
def toolow():
    return render_template('toolow.html')

@app.route('/toohigh')
def toohigh():
    return render_template('toohigh.html')

@app.route('/success')
def success():
    return render_template('correct.html')

@app.route('/again', methods=['post'])
def again():
    return redirect('/')

app.run(debug=True)