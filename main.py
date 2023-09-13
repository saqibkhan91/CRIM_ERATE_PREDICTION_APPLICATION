
from pred import crime_prediction
from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/')
def index():
    return  render_template('home.html')



@app.route('/predict',methods=['GET','POST'])
def predict():
    cityname=request.form.get('cityname')
    year=request.form.get('year')
    crimetype=request.form.get('crimetype')
    pred=crime_prediction(cityname,crimetype,int(year))
    pred=round(pred)
    return  render_template('home.html',prediction=pred)



if __name__ == "__main__":
    app.run(debug=True)   
