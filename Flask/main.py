from flask import Flask
app =Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/Champion')
def champion():
    return "Champion!"
@app.route('/say/<name>')
def say(name):
    return f"Hi {name.capitalize()}"

@app.route('/say/<int:num>/<word>')
def repeat(num,word):
    return (word+ " ") * num

@app.errorhandler(404)
def not_found(e):
   return "Sorry! No response. Try again .",404
if __name__=="__main__":
    app.run(debug=True,port=5001)
