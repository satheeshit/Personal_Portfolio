from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'rsatheeshit@gmail.com'       # Your Gmail
app.config['MAIL_PASSWORD'] = 'jjzpdhcqzuioegji'          # App password, not your Gmail password

mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Send email
        msg = Message(subject=f"New message from {name}",
                      sender=app.config['MAIL_USERNAME'],
                      recipients=[app.config['MAIL_USERNAME']],
                      body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}")
        mail.send(msg)

        flash("Your message was sent successfully!")
        return redirect(url_for('home'))

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
