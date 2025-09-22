from flask import Flask,render_template,request,jsonify
app = Flask(__name__)
def chatbot_response(user_input):
    responses={
        "hi":"Hello! How can I assist you today?",
        "how are you?":"I'm doing great 😁",
        "bye":"Goodbye! Have a great day!",
        "what is your name?":"I am Maddy, your friendly chatbot."
    }
    return responses.get(user_input.lower(),"I'm sorry, I don't understand that.")
@app.route("/") 
def home():
    return render_template("index.html")    
@app.route("/get",methods=["POST"])
def get_bot_response():
    user_input=request.json["message"]
    response=chatbot_response(user_input)
    return jsonify({"reply":response})   
if __name__=="__main__":
    app.run(debug=True)