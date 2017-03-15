from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('login.html')

@app.route('/foo')
def button():
    name = "have nice day"
    return render_template('login.html', word=name)


@app.route('/success/<name>')
def success(name="ebla"):
   return render_template('login.html', nameGET=name)

@app.route('/hello/', methods=['POST','GET'])
def hello():
    if request.method == 'POST':
        name=request.form['nm']
        return render_template('login.html', name=name)
    else:
        nameGET = request.args.get('q')
        return redirect(url_for('success', name=nameGET))

if __name__ == "__main__":
    app.run()