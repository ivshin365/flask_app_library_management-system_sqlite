from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, RadioField, DateField
from wtforms.validators import DataRequired

# A class is created for each form required
class TestForm(FlaskForm):
	genders = [
		('male', 'Male'),
		('female', 'Female')
	]

	projects = [
		('hh1', 'HH1'),
		('hh2', 'HH2'),
		('manpack', 'MANPACK'),
		('va', 'VA'),
		('vic', 'VIC'),
		('hf', 'HF WB'),
		('rdt', 'RDT'),
		('vic', 'VIC'),
		('iris', 'IRIS'),
		('pnr', 'PNR'),
		('connectors', 'CONNECTORS'),
		('general', 'GENERAL COMPONENTS'),
	]

	name = StringField('Name', validators=[DataRequired()])
	part = StringField('Part Number', validators=[DataRequired()])
	description = StringField('Component Description', validators=[DataRequired()])
	project = SelectField('Project', choices=projects, validators=[DataRequired()])
	location = StringField('Location', validators=[DataRequired()])
	submit = SubmitField('Submit')
