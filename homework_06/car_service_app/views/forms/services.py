from flask_wtf import FlaskForm
from wtforms import StringField, URLField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, URL


class ServiceForm(FlaskForm):
    name = StringField(
        label="Service name",
        name="service-name",
        validators=[DataRequired(), Length(min=3, max=80)],
        render_kw={"placeholder": "some service..."},
    )

    description = TextAreaField(
        label="Service description",
        name="service-description",
        validators=[Length(min=16, max=256)],
        render_kw={"placeholder": "some service description..."},
    )

    image = URLField(
        label="Image field",
        name="image-field",
        validators=[URL()],
        render_kw={"placeholder": "https://url_of_your_image.com/example.png"},
    )

    free_car_wash = BooleanField(
        label="Free car wash",
        name="free-car-wash",
        default=False,
    )
