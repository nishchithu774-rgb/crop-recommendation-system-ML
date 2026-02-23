from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load model
model = pickle.load(open("crop_model.pkl","rb"))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():

    try:
        # Convert input to float
        N = float(request.form['N'])
        P = float(request.form['P'])
        K = float(request.form['K'])
        temp = float(request.form['temp'])
        humidity = float(request.form['humidity'])

        # Prediction
        prediction = model.predict([[N,P,K,temp,humidity]])

        return render_template("result.html",
                               crop=prediction[0])

    except:
        return render_template("index.html",
                               error="❌ Invalid Input! Enter numbers only.")



if __name__ == '__main__':
    app.run(debug=True)