# Bike sharing prediction model API

## Juan David Botero

## Usage

This package creates a model to predict bike-sharing demand given some weather paremeters and a model parameter to predict.

In order to clone this repository you need to follow this command in your terminal:

```
$ git clone https://github.com/JuanDavidBotero/ie-bike-sharing-model-lib-JDB.git
```
After that you have to look for the folder created inside your computer and move to that folder
```
$ cd ie-bike-sharing-model-lib-JDB
```
**Once in that folder follow the next instructions:**

To install the library developed:

```
$ # pip install ie_bike_model  # If I ever upload this to PyPI, which I won't
$ pip install .
```

Basic usage:

```python
>>> import datetime as dt
>>> from ie_bike_model.model import train_and_persist, predict
>>> train_and_persist()
>>> predict({
...     "date": dt.datetime(2011, 1, 1, 0, 0, 0),
...     "weathersit": 1,
...     "temperature_C": 9.84,
...     "feeling_temperature_C": 14.395,
...     "humidity": 81.0,
...     "windspeed": 0.0
... })
1
```

## Development

To install a development version of the library:

```
$ flit install --symlink --extras=dev
```

To run the tests:

```
$ pytest
```

To measure the coverage:

```
$ pytest --cov=ie_bike_model
```

## Trivia

Total implementation time: **4 hours 30 minutes** 🏁

## To run the API (located on app.py) on your localhost run:

```
$ flask run
```
Output:
* Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 
 ### Now you have 3 choices of the model parameter xgboost, ridge, lasso (no quotes):
 - Follow this link to get a prediction with some weather parameter and a specific model: http://127.0.0.1:5000/predict?date=2012-10-01T18:00:00&weathersit=1&temperature_C=15&feeling_temperature_C=14&humidity=20&windspeed=5&model=ridge
 
 - Follow this link to get the training score of the model: http://127.0.0.1:5000/score?model=ridge 
   - {"Train score":0.9104886886576075} **xgboost**
   - {"Train score":0.7523794629159768} **ridge**
   - {"Train score":0.30553692054467785} **lasso**

# Thanks!
