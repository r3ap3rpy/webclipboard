from flask import Flask, request, abort
from functools import wraps
from datetime import datetime, timedelta
import sys 
import hashlib

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
	return 	e, 404

ResponseCache = {}
@app.route("/clipboard",methods = ['GET'])
def get_content():
	Calc = hashlib.sha512((str(request.authorization.username)+str(request.authorization.password)).encode('utf-8')).hexdigest()
	if ResponseCache.get(Calc):
		if datetime.strptime(ResponseCache[Calc]['Expiry'],"%Y-%m-%d %H:%M:%S.%f") < datetime.now():
			abort(404, "Content has expired {} minutes ago!".format((datetime.now() - datetime.strptime(ResponseCache[Calc]['Expiry'],"%Y-%m-%d %H:%M:%S.%f")).seconds))
		else:
			return str(ResponseCache[Calc]['Content'])
	else:
		abort(404, "You do not have any content on your clipboard!")


@app.route("/clipboard", methods = ['POST'])
def set_content():
	if not request.form.get('Content'):
		abort(404, "No Content")
	if not request.form.get('User'):
		abort(404, "No User")
	if not request.form.get('Pwd'):
		abort(404, "No Password")
	if not request.form.get('Expiry'):
		delta = 60 *5
	else:
		delta = 60 * int(request.form.get('Expiry'))

	ResponseCache.update({hashlib.sha512((str(request.form.get('User'))+str(request.form.get('Pwd'))).encode('utf-8')).hexdigest():{'Content':request.form['Content'],'Expiry':str(datetime.now() + timedelta(seconds=delta))}})
	print(ResponseCache)
	return "Success", 200
	
app.run(host='0.0.0.0', port=10000, debug=True)

