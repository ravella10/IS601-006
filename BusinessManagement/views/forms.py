from flask_wtf import FlaskForm
from wtforms import EmailField, SubmitField, StringField
from wtforms.validators import DataRequired, Email, InputRequired, Length, regexp

class CompanyForm(FlaskForm):
    name = StringField("Name")
    address = StringField("Address")
    city = StringField("City")
    zip = StringField("Zip")
    website = StringField("Website")
    submit = SubmitField("Add Company")

class EmployeeForm(FlaskForm):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    email = EmailField("Email")
