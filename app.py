from flask import Flask,jsonify,request
from predict import predicts 
import joblib

app = Flask(__name__)
model = joblib.load('./models/model_M_B.pkl')

@app.route('/<isbn>')
def greets(isbn):
    return "Welcome to the Prediction API"

@app.route('/diagnosis', methods=['POST'])
def diagnosis():
    data = request.get_json()
    x = data['input']
    
    try:
        result = predicts(data, model)
        return jsonify({'result':result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

    
    
    

    
if __name__ == '__main__':
    app.run(debug=True)