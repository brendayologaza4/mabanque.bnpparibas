
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegistrationForm(FlaskForm):
    full_name = StringField(
        'Nom complet',
        validators=[
            DataRequired(message="Ce champ est obligatoire."),
            Length(min=2, max=100, message="Le nom doit faire entre 2 et 100 caractères.")
        ]
    )

    email = StringField(
        'Adresse email',
        validators=[
            DataRequired(message="Ce champ est obligatoire."),
            Email(message="Adresse email invalide.")
        ]
    )

    password = PasswordField(
        'Mot de passe',
        validators=[
            DataRequired(message="Ce champ est obligatoire."),
            Length(min=6, message="Le mot de passe doit faire au moins 6 caractères.")
        ]
    )

    confirm_password = PasswordField(
        'Confirmer le mot de passe',
        validators=[
            DataRequired(message="Ce champ est obligatoire."),
            EqualTo('password', message="Les mots de passe doivent correspondre.")
        ]
    )

    submit = SubmitField('Créer un compte')


class LoginForm(FlaskForm):
    email = StringField(
        'Adresse email',
        validators=[
            DataRequired(message="Ce champ est obligatoire."),
            Email(message="Adresse email invalide.")
        ]
    )

    password = PasswordField(
        'Mot de passe',
        validators=[
            DataRequired(message="Ce champ est obligatoire.")
        ]
    )

    submit = SubmitField('Connexion')