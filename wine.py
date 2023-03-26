from flask import Flask,render_template,request
from utils import wineprediction
import traceback

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data', methods = ['POST','GET'])
def get_data():
    try: 
        if request.method == "POST":
            data = request.form
            class_obj = wineprediction(data)
            result = class_obj.get_wine_quality_prediction()
            x = None
            if result == 1 :
                x="Good Quality Wine"
            else:
                x="Bad Quality Wine"
        
            return render_template('index.html',prediction = x)
        else: 
            print(f"wrong method")
            return "Wrong method"
    except:
       print(traceback.print_exc())
       return "Prediction Unsuccessful"


if __name__ == "__main__":
    app.run(host = '0.0.0.0')