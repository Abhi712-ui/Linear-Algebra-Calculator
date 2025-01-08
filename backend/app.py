from flask import Flask, request, jsonify

'''
flask - the core framework

request - used to handle incoming data from requests

jsonify - flask utility used to create JSON responses
'''
app = Flask(__name__)

'''
Flask(__name__) - creating an instance of the flask application

__name__ - the argument that we pass to the flask application instance that we just created, this allows it to locate
resources relative to the application script, such as templates and static files
'''


@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "backend is running!"})


'''
@app.route('/api') - registers a new route with the application, this format is called a decorator

api slash health - the url for the new route that we created, and we use GET to specify that this responds to 
GET HTTP requests

def health_check() - the function that runs when this URL is accessed through a GET request

jsonify - turns the dictionary input we gave into a JSON response to display
'''

if __name__ == '__main__':
    app.run(debug=True)


'''
if __name__ == '__main__': - this is used to make sure that this only runs when the app.py file is run itself directly, 
and not as part of an imported module

app.run(debug=True) - starts the flask development server, and enables debug mode, reloading whenever you make changes,
and displays errors to the screen
'''
