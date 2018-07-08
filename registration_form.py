from flask import Flask, render_template, redirect, request, flash
app = Flask(__name__)
app.secret_key = "boobookittycluck"
@app.route('/')
def index():
    return render_template('registration_form.html')

@app.route('/process', methods=['POST'])
def process():
    # Block that checks if all form fields are populated
    if len(request.form['email'])< 1:
        flash('Email field required!', 'error')
    elif len(request.form['first_name'])< 1:
        flash('First name field required!', 'error')
    elif len(request.form['last_name'])< 1:
        flash('Last name field required!', 'error')
    elif len(request.form['password']) < 1:
        flash('Password field required!', 'error')
    elif len(request.form['confirm_password'])< 1:
        flash('Confirm field required!', 'error')
    elif len(request.form['password']) < 9:
        flash('Password minimum 9 characters!')
    elif request.form['password'] != request.form['confirm_password']:
        flash('Passwords must match!')
    return redirect('/')

    


if __name__ == '__main__':
    app.run(debug=True)
