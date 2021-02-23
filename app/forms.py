from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename

class uploadForm(FlaskForm):
    image = FileField('photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'])])