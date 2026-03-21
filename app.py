from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, TimeField, SubmitField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

class ConsultationForm(FlaskForm):
    symptoms = TextAreaField('症状描述', validators=[DataRequired(), Length(min=10, max=500)])
    name = StringField('姓名', validators=[DataRequired(), Length(min=2, max=50)])
    phone = StringField('手机', validators=[DataRequired(), Length(min=11, max=11)])
    birth_date = DateField('出生日期', format='%Y-%m-%d', validators=[DataRequired()])
    birth_time = TimeField('出生时间', format='%H:%M', validators=[DataRequired()])
    submit = SubmitField('提交问诊')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consultation', methods=['GET', 'POST'])
def consultation():
    form = ConsultationForm()
    if form.validate_on_submit():
        # 这里可以处理表单数据，比如保存到数据库
        return render_template('consultation_success.html')
    return render_template('consultation.html', form=form)

@app.route('/moxibustion')
def moxibustion():
    return render_template('moxibustion.html')

@app.route('/appointment')
def appointment():
    return render_template('appointment.html')

if __name__ == '__main__':
    app.run(debug=True)
