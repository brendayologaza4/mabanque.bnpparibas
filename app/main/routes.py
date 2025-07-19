
from flask import render_template, request, flash, redirect, url_for
from app.main import main_bp
from app.main.forms import ContactForm
from app.email_utils import send_email

@main_bp.route('/')
@main_bp.route('/home')
def home():
    return render_template('main/home.html')

@main_bp.route('/comptes')
def comptes():
    return render_template('main/comptes.html')

@main_bp.route('/cartes')
def cartes():
    return render_template('main/cartes.html')

@main_bp.route('/emprunts')
def emprunts():
    return render_template('main/emprunts.html')

@main_bp.route('/assurances')
def assurances():
    return render_template('main/assurances.html')

@main_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Envoi du message au mail admin
        send_email(
            subject=f"Message du site de {form.name.data}",
            recipients=['thanosford@proton.me'],
            template='emails/contact.html',
            name=form.name.data,
            email=form.email.data,
            message=form.message.data
        )
        flash('Merci pour votre message, nous vous répondrons rapidement.', 'success')
        return redirect(url_for('main.contact'))

    return render_template('main/contact.html', form=form)