from flask import Flask, redirect, url_for, render_template, request


#Configure Flask app
app = Flask(__name__)
application = app



#Login page
#@app.route('/login', methods=['GET', 'POST'])
#def login():
#	error = None
#	if request.method == 'POST':
#		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
#			error = 'Invalid Credentials. Please Try Again!'
#	else: return redirect(url_for('home'))
#	return render_template('login.html', error = error)	




@app.route('/')
def index():
	return render_template('index.html')

@app.route('/calculatrice', methods=['GET', 'POST'])
def foodweek():

	return render_template('foodweek.html')


@app.route('/manques', methods=['GET', 'POST'])
def manques():

	return render_template('manques.html')


"""@app.route('/inputform', methods=['GET', 'POST'])
def inputform():
	error = None
	
	if request.method == 'POST':
		foodname = request.form['foodname']
		foodname = foodname.lower()
		print(foodname)
		quantity = request.form['quantity']
		print(quantity)
		day = request.form['day']
		print(day)
		patate = 'vive les patates'
		
		key = 'allow'

		'''if day == 'Monday':
			for nutrient in humanMonday:
				missing_protein = '''

		return render_template('foodweek.html', foodname=foodname, quantity=quantity, key=key, day=day, patate=patate)

	return render_template('inputform.html', error=error)
"""



if __name__ == '__main__':
	app.run()
	
