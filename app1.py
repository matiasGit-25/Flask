from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
	return "Hello World!"
	
@app.route('/hithere')
def hi_there_everyone():
	return "I just hit /hithere"
	
@app.route('/bye')
def bye():
	#Prepare a response for the request that came to /bye
	c = 2*534
	s = str(c)
	retJson = {
		'field1':'abc',
		'field2':'def'
	}
	return jsonify(retJson)

if __name__=="__main__":
	app.run(debug=True, host="127.0.0.1", port=80)