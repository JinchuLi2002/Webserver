from flask import Flask, render_template
from flask_caching import Cache

app = Flask(__name__)
# Configure cache
# Consider using 'Redis' or another cache type for production
app.config['CACHE_TYPE'] = 'SimpleCache'
app.config['CACHE_DEFAULT_TIMEOUT'] = 300  # Cache timeout in seconds

cache = Cache(app)


@app.route('/')
@cache.cached(timeout=50)  # Cache this view for 50 seconds
def home():
    return render_template('p1.html')


@app.route('/page2')
@cache.cached(timeout=50)
def page2():
    return render_template('p2.html')


@app.route('/page3')
@cache.cached(timeout=50)
def page3():
    return render_template('p3.html')


@app.route('/page4')
@cache.cached(timeout=50)
def page4():
    return render_template('p4.html')


@app.route('/page5')
@cache.cached(timeout=50)
def page5():
    return render_template('p5.html')


if __name__ == '__main__':
    # Runs on http://localhost:5500 by default
    app.run(host='0.0.0.0', port=5500)
