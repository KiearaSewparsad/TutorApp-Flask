import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')  # absolute path
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # Max 5 MB

applications = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
        email = request.form.get('email')
        phone = request.form.get('phone')
        subjects = request.form.get('subjects')
        experience = request.form.get('experience')

        cv = request.files['cv']
        cv_filename = ''
        if cv:
            cv_filename = cv.filename
            cv.save(os.path.join(app.config['UPLOAD_FOLDER'], cv_filename))

        applications.append({
            'name':name,
            'surname':surname,
            'email':email,
            'phone':phone,
            'subjects':subjects,
            'experience':experience,
            'cv':cv_filename
        })
        return redirect(url_for('thank_you'))
    return render_template('index.html')

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True)