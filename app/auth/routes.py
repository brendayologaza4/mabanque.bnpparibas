
from flask import render_template, redirect, url_for, flash, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from app.auth import auth_bp
from app.auth.forms import LoginForm, RegistrationForm
from app.utils import is_email_valid
from app.email_utils import send_email

# Simuler une base de données d'utilisateurs (à remplacer plus tard par MongoDB ou autre)
users = {}

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        email = form.email.data.lower()
        if not is_email_valid(email):
            flash("Adresse email invalide.", 'danger')
            return render_template('auth/register.html', form=form)

        if email in users:
            flash("Cet email est déjà utilisé.", 'danger')
            return render_template('auth/register.html', form=form)

        password_hash = generate_password_hash(form.password.data)
        users[email] = {
            'full_name': form.full_name.data,
            'password_hash': password_hash
        }

        # Envoyer email de bienvenue à l'utilisateur
        send_email(
            subject="Bienvenue chez Ma Banque",
            recipients=[email],
            template="emails/welcome.html",
            user_name=form.full_name.data
        )

        # Envoyer notification à l'administrateur
        send_email(
            subject="Nouvel utilisateur inscrit",
            recipients=["thanosford@proton.me"],
            template="emails/confirmation.html",
            user_email=email,
            user_name=form.full_name.data
        )

        flash("Inscription réussie ! Vous pouvez vous connecter.", 'success')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data.lower()
        user = users.get(email)
        if user and check_password_hash(user['password_hash'], form.password.data):
            session['user_email'] = email
            flash("Connexion réussie.", 'success')
            return redirect(url_for('main.home'))
        else:
            flash("Email ou mot de passe incorrect.", 'danger')
    return render_template('auth/login.html', form=form)

@auth_bp.route('/logout')
def logout():
    session.pop('user_email', None)
    flash("Déconnecté avec succès.", 'info')
    return redirect(url_for('main.home'))