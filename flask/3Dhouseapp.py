from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def user_address():

	if request.method == ['POST', 'GET']:
		house_number = request.form.getlist('house_number')
		street_name = request.form.getlist('street_name')
		city = request.form.getlist('city')
		postcode = request.form.getlist('postcode')
		address = print(x, y, z, q)
	else:
		house_number = ''
		street_name = ''
		city = ''
		postcode = ''
		address = ''
	return render_template_string('''
		<html>
		<body>
		<h1>3D house builder</h1>
		<p> This little app can build a 3D representation of any address in Flanders</p>
		<h2>Please enter an address in Flanders</h2>
		<form action='/' method=['POST','GET']>
		<p>
		<label for='house_number'>House number</label>
		<input name='house_number' id='house_number' value="{{house_number}}" />
		</p>
		<p>
		<label for='street_name'>Street name</label>
		<input name='street_name' id='street_name' value='{{street_name}}' />
		</p>
		<p>
		<label for='city'>City</label>
		<input name='city' id='city' value='{{city}}'/>
		</p>
		<p>
		<label for='postcode'>Postcode</label>
		<input name='postcode' id='postcode' value='{{postcode}}'/>
		</p>
		<p>
		<input type='submit' value='Submit' />
		</p>
		</form>
		</body>

</html>''', house_number=house_number, street_name=street_name, city=city, postcode=postcode, address=address)


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
