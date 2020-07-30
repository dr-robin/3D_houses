from flask import Flask
from flask import Flask, request, render_template_string
import make3dh

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
    
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        house_number = request.form.get('house_number')
        street_name = request.form.get('street_name')
        city = request.form.get('city')
        postcode = request.form.get('postcode')

        #need to delete return
        #return '''<h1>The house number is: {}</h1>
         #   <h1>The street is: {}</h1>
          #  <h1>The city is: {}</h1>
           # <h1>The postcode is: {}</h1>
            #'''.format(house_number, street_name, city, postcode)
        
        #try build 3D house function here
        try:
            make_house()
            
        except IndexError:
            print("Please enter an address in Flanders")
            
        except:
            print("Please try again")
            
            exit()
    #else return empty form variables
        #else:
         #   house_number = ''
          #  street_name = ''
           # city = ''
            #postcode = ''

    #Landing page with user address form
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <title>3D house builder</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    </head>
    <body>
    <div class="container">
    <img src="./house.svg" alt="house"> 
    </div>
    <div class="container-fluid">
    <div class="jumbotron">
    <h1>3D house builder</h1>
    </div>
    <div class="container-fluid">
    <h4>This little app can build a 3D representation of any address in Flanders</h4>
    <p>Enter address</p>
    <form method='POST'>
    <input type='number' name='house_number'/>
    <input type='text' name='street_name'/>
    <input type='text' name='city'/>
    <input type='number' name='postcode'/>
    <input type='submit' value='Submit'/>
    </p>
    </form>
    </div>
    </body>
    </html>'''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
# <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
# <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
#use for warnings <div class="alert alert-danger">
