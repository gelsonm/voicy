from flask import Flask, request, render_template
from your_voice_assistant_file import VoiceAssistant  # Replace with your actual file name

app = Flask(__name)

# Initialize the voice assistant
assistant = VoiceAssistant()

@app.route('/')
def home():
    return render_template('index.html')  # Create an HTML file for the interface

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']
    
    if user_input.strip().lower() == "goodbye":
        response = "Goodbye! Have a great day!"
    else:
        response = assistant.think(user_input)
    
    assistant.speak(response)
    
    return render_template('index.html', user_input=user_input, response=response)

if __name__ == '__main__':
    app.run(debug=True)
