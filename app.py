from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        initial_value = float(request.form['initial_value'])
        final_value = float(request.form['final_value'])
        years = float(request.form['years'])
        cagr = ((final_value / initial_value) ** (1 / years) - 1) * 100
        result = f"{cagr:.2f}"
    return render_template('index.html', result=result)

    if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

