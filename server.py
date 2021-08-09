from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    customer_name = f"{request.form['first_name']} {request.form['last_name']}"
    count = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    print(f'Charging {customer_name} for {count} fruits')
    return render_template("checkout.html", count=count)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    