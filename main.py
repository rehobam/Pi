from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Директория для загрузки фото
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        # Получаем данные из формы
        brand = request.form['Марка машины']
        year = request.form['Год пройзводство']
        color = request.form['Цвет']
        price = request.form['Цена']
        photo = request.files['Фото']

        # Сохраняем фото
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo.filename))

        # Добавляем другие данные в базу данных или выполняем другие действия

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)