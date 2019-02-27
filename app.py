from flask import Flask, render_template, request, redirect, url_for
from common.database import save_suggestions_to_db, load_suggestions_from_db

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('suggestions.html', suggestions=suggestions)


@app.route('/new', methods=['POST'])
def new_suggestion():
    data = request.form.get('suggestion')
    suggestions.append(data)
    save_suggestions_to_db(suggestions)

    return redirect(url_for('.home'))

if __name__ == '__main__':
    global suggestions
    suggestions = load_suggestions_from_db()
    app.run(debug=True)
