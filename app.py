from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/location')
def location():
    return jsonify({
        "lat": round(19.0760 + random.random() / 100, 6),
        "lon": round(72.8777 + random.random() / 100, 6)
    })

if __name__ == '__main__':
    app.run(debug=True)