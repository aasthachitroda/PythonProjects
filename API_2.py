from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def Home():
    return "Home Page"

@app.route('/armstrong/<int:n>')
def armstrong(n):
    sum = 0
    order = len(str(n))
    copy_n = n
    while(n>0):
        digit = n%10
        sum += digit **order
        n = n//10

    if (sum == copy_n):
        result = {
            "Number": copy_n,
            "Armstrong": True
        }
    else:
        result = {
            "Number": copy_n,
            "Armstrong": False
        }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)