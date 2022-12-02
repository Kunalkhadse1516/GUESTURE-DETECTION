
from flask import Flask, render_template, redirect
import Hand_gesture_detection as HG
import virtual_paint_app as VP
app = Flask(__name__)

@app.route("/")
def interface():
    return render_template('interface.html')

@app.route("/GestureInterface")
def gesture_interface():
    return render_template('gesture_interface.html')

@app.route("/PainterInterface")
def painter_interface():
    return render_template('painter_interface.html')

@app.route("/Enter")
def HAND():
    HG.callfunction()
    return redirect('/')

@app.route("/enter")
def PAINT():
    VP.callfun()
    return redirect('/')
    

if __name__=="__main__":
    app.run(debug=True)


