from flask import Flask
#from useraddress import get_address

from flask import Flask, request, render_template_string

app = Flask(__name__)
    
@app.route('/', methods=['GET','POST'])
def index():
	if request.method == 'POST':
		house_number = request.form.get('house_number')
		street_name = request.form.get('street_name')
		city = request.form.get('city')
		postcode = request.form.get('postcode')
		
		#need to delete return
		return '''<h1>The house number is: {}</h1>
			<h1>The street is: {}</h1>
			<h1>The city is: {}</h1>
			<h1>The postcode is: {}</h1>
			'''.format(house_number, street_name, city, postcode)
		#try build 3D house function here
		
		
	#else return empty form variables
	else:
		house_number = ''
		street_name = ''
		city = ''
		postcode = ''

	#Landing page with user address form
	return '''
	<html>
	<body>
	<h1>3D house builder</h1>
	<p> This little app can build a 3D representation of any address in Flanders</p>
	<h2>Please enter an address in Flanders</h2>
	<form method='POST'>
	<input type='number' name='house_number'/>
	<input type='text' name='street_name'/>
	<input type='text' name='city'/>
	<input type='number' name='postcode'/>
	<input type='submit' value='Submit'/>
	</p>
	</form>
	</body>
	</html>'''

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
