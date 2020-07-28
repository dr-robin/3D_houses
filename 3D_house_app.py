from flask import Flask
#from useraddress import get_address

from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def user_address():

	if request.method == 'POST':
		house_number = request.form.get('house_number')
		street_name = request.form.get('street_name')
		city = request.form.get('city')
		postcode = request.form.get('postcode')
		
		#return success
		#add 3D house builder function here
		return '''success'''

	#else return empty form variables
	else:
		house_number = ''
		street_name = ''
		city = ''
		postcode = ''

	#Landing page with user address form
	return render_template_string('''
	<html>
	<body>
	<h1>3D house builder</h1>
	<p> This little app can build a 3D representation of any address in Flanders</p>
	<h2>Please enter an address in Flanders</h2>
	<form method='POST'>
	<p>
	<label for='house_number'>House number</label>
	<input name='house_number' id='house_number' value='' />
	</p>
	<p>
	<label for='street_name'>Street name</label>
	<input name='street_name' id='street_name' value='' />
	</p>
	<p>
	<label for='city'>City</label>
	<input name='city' id='city' value='' />
	</p>
	<p>
	<label for='postcode'>Postcode</label>
	<input name='postcode' id='postcode' value='' />
	</p>
	<p>
	<input type='submit' value='Submit' />
	</p>
	</form>
	</body>
	</html>''')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
