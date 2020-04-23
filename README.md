# IITKBucks

The webserver.py contains code for a web server in flask framework. To start the server, git clone the repository (or download the .py file) and run the script in command prompt using the command - python webserver.py in the relevant directory. 
The output shall be as shown - 
* Serving Flask app "webserver" (lazy loading)
* Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
* Debug mode: off
* Running on http://127.0.0.1:8787/ (Press CTRL+C to quit)

This means the server has started. 

You can send a post request to it at http://127.0.0.1:8787/hash in json format - {"data" : "<your_string>" }
