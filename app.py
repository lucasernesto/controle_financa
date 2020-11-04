from flask import Flask, render_template
from forms.forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasecretkey'

@app.route("/form", methods=['GET', 'POST'])
def form():
    form = LoginForm()

    if form.validate():
        return 'The form has beem submit'
    return render_template('form.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)