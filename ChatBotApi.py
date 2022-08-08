from flask import Flask, request, jsonify

from chatbot import predict_class, get_response, intents

my_intents = intents

app = Flask(__name__)

@app.route('/chat', methods=['GET', 'POST'])
def predictClass():
    chatInput = request.form['chatInput']
    ints = predict_class(chatInput)
    return jsonify(chatBotReply=get_response(ints, my_intents))

if __name__ == '__main__':
    app.run(debug=True)