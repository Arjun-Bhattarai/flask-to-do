from flask import Flask, render_template     #flask library import garako 

first = Flask(__name__)        #index file banako Creates your Flask app. __name__ tells Flask where to find files and routes.

@first.route('/')         # route defing gaeako link jasti kata jane vanara ('/home or about ')
def helloworld():            #function banako 
    return render_template('index.html')          
    return 'Hello, this is my first Flask program!'     #k show garne 

@first.route('/about')
def about():
    return 'aasari aarko page ma jana sakinxa '

if __name__ == "__main__":        #execut garda nai code run hos ko lagi
    first.run(debug=True)        # error haru chai terminal mai dekhiyos
