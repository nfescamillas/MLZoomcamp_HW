import pickle
from flask import Flask 
from flask import request
from flask import jsonify 


from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer


with open("dv.bin",'rb') as fin_dv:
    dv = pickle.load(fin_dv)


with open("model1.bin",'rb') as fin_model:
    model = pickle.load(fin_model)


app = Flask('Subscription')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    subscription= y_pred >= 0.5

    result = {
        'subscription_probability': float(y_pred),
        'subscription': bool(subscription)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)