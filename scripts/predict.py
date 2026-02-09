import pickle
from flask import  Flask, request, jsonify

with open('/workspaces/churn-analysis/models/model_c1.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)


app = Flask('churn')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
    X = dv.transform([customer])
    churn_prob = model.predict_proba(X)[0, 1]
    churn = churn_prob >= 0.4

    result = {
        'churn_probability': churn_prob,
        'churn': bool(churn)
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)