import datetime as dt
from flask import Flask, request

from ie_bike_model.model import predict, train_and_persist

app = Flask(__name__)


@app.route("/")
def hello():
    name = request.args.get("name", "World")
    return "Hello, " + name + "!"


@app.route("/predict")
def get_predict():
    parameters = dict(request.args)
    parameters["date"] = dt.datetime.fromisoformat(parameters["date"])
    parameters["weathersit"] = int(parameters["weathersit"])
    parameters["temperature_C"] = float(parameters["temperature_C"])
    parameters["feeling_temperature_C"] = float(parameters["feeling_temperature_C"])
    parameters["humidity"] = float(parameters["humidity"])
    parameters["windspeed"] = float(parameters["windspeed"])
    parameters["model"] = parameters["model"]

    result = predict(parameters, model=parameters["model"])
    return {
        "Number of bike-users predicted": result,
        "model": parameters["model"],
        "test score": "Unkown...",
    }


@app.route("/score")
def get_train_score():
    parameters = dict(request.args)
    parameters["model"] = parameters["model"]
    score = train_and_persist(model=parameters["model"])

    return {"Train score": score}
