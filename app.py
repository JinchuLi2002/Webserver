from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('p1.html')


@app.route('/page2')
def page2():
    return render_template('p2.html')


@app.route('/page3')
def page3():
    return render_template('p3.html')


@app.route('/page4')
def page4():
    return render_template('p4.html')


@app.route('/page5')
def page5():
    return render_template('p5.html')

# Add similar routes for page3, page4, and page5


if __name__ == '__main__':
    # Runs on http://localhost:5000 by default
    app.run(host='0.0.0.0', port=5500)
