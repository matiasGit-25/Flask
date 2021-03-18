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
	age = 14*2+1
	s = str(c)
	retJson = {
		'Name': 'Mati',
		'Age': age,
		"Phones":[
			{
				"phoneName": "Samsung",
				"phoneNumber": 12345123
			},
			{
                                "phoneName": "Samsung",
                                "phoneNumber": 43214321
			}
		]
	}
	return jsonify(retJson)

if __name__=="__main__":
	app.run(debug=True)