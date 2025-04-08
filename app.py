# Registration Numbers: 12301663, 12303679

from flask import Flask, render_template, request, jsonify
from chatbot import TravelBudgetBot
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key-here')

# Initialize chatbot
chatbot = TravelBudgetBot()

@app.route('/')
def index():
    registration_numbers = "12301663, 12303679"
    return render_template('chat.html', registration_numbers=registration_numbers)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = chatbot.process_message(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True) 