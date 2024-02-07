from flask import Flask, render_template, request
from gemini_pro import gemini_pro_text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the text input value from the form
        text_input = request.form['text_input']
        response = gemini_pro_text.generate_content([text_input]).text
    return render_template('index.html', input_text = response)


if __name__ == '__main__':
    app.run(debug=True)