from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

suggestions = [
    'Add content on design patterns with Python',
    'Cover more algorithms',
    'Start live streaming'
]

@app.route('/')
def home():
    return render_template('suggestions.html', suggestions=suggestions)


@app.route('/new', methods=['POST'])
def new_suggestion():
    data = request.form.get('suggestion')
    suggestions.append(data)

    return redirect(url_for('.home'))

if __name__ == '__main__':
    app.run(debug=True)
