from flask import Flask, Response, request
import functions_framework
from run import *

app = Flask(__name__)

@app.route('/text_to_gif')
def text_to_gif():
    text = request.args.get('text')
    gif = run_code(text)
    if gif:
        return Response(gif, mimetype='image/gif')
    else:
        return "Gif cannot be generated because none of the words is in the database", 500
    
if __name__== "__main__":
    app.run()
