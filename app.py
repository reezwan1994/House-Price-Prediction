import joblib
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Load the trained model
model = joblib.load('best_tree_model.pkl')

# Homepage with input form
@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>House Price Prediction</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 50px; text-align: center; }
            form { display: inline-block; text-align: left; padding: 20px; border: 1px solid #ccc; border-radius: 10px; background: #f9f9f9; }
            input { margin-bottom: 10px; width: 100%; padding: 8px; }
            button { padding: 10px 20px; background: #28a745; color: white; border: none; cursor: pointer; }
            button:hover { background: #218838; }
        </style>
    </head>
    <body>
        <h2>House Price Prediction</h2>
        <form action="/predict" method="post">
            <label>MedInc: <input type="text" name="MedInc" required></label><br>
            <label>HouseAge: <input type="text" name="HouseAge" required></label><br>
            <label>AveBedrms: <input type="text" name="AveBedrms" required></label><br>
            <label>Population: <input type="text" name="Population" required></label><br>
            <label>AveOccup: <input type="text" name="AveOccup" required></label><br>
            <label>Latitude: <input type="text" name="Latitude" required></label><br>
            <label>Longitude: <input type="text" name="Longitude" required></label><br>
            <button type="submit">Predict</button>
        </form>
    </body>
    </html>
    '''

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from form submission
        input_features = [
            float(request.form['MedInc']),
            float(request.form['HouseAge']),
            float(request.form['AveBedrms']),
            float(request.form['Population']),
            float(request.form['AveOccup']),
            float(request.form['Latitude']),
            float(request.form['Longitude'])
        ]

        # Make prediction
        prediction = model.predict([input_features])[0]*100000 # Multiply by 100,000

        return f'''
        <html>
        <head>
            <title>Prediction Result</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 50px; text-align: center; }}
                .result-box {{ display: inline-block; padding: 20px; border: 1px solid #ccc; border-radius: 10px; background: #f9f9f9; }}
                a {{ display: block; margin-top: 20px; text-decoration: none; color: #007bff; }}
                a:hover {{ text-decoration: underline; }}
            </style>
        </head>
        <body>
            <div class="result-box">
                <h2>Predicted House Price: ${prediction:,.2f}</h2>
                <a href="/">Go Back</a>
            </div>
        </body>
        </html>
        '''
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
