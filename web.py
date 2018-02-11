from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("content.html")

@app.route('/About/')
def About():
    return render_template("About.html")


if __name__=="__main__":
  app.run(debug=True)  
