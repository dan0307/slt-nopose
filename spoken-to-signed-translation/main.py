from flask import Flask, Response, request, jsonify
import functions_framework
from run import *

app = Flask(__name__)

@app.route('/')
def text_to_gif():
    text = request.args.get('text')
    print(text)
    gif = run_code(text)
    if gif:
        return Response(gif, mimetype='image/gif'), 200
    else:
        msg = "Gif cannot be generated because none of the words is in the database for the words " + text 
        #with open("no_translation.gif","rb") as f:
        #    gif_notrans=f.read()
        #return Response(gif_notrans, mimetype='image/gif'), 418
        data = {
            'message': 'No GIF could be created - None of the words could be translated'
        }
        
        # Returning a tuple with response data and status code
        return jsonify(data), 418

    
if __name__== "__main__":
    app.run(host="0.0.0.0", port=int("8000"), debug=True)
