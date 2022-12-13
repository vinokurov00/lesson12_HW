import logging

from flask import Blueprint, render_template, request
from json import JSONDecodeError
from functions import add_post
from loader.utils import save_picture

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/post/')
def post_page():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def add_post_page():
    picture = request.files.get('picture')
    content = request.form.get('content')

    if not picture or not content:
        return 'No pic or text'
    if picture.filename.split('.')[-1] not in ['jpeg', 'png']:
        logging.info('Загружена не картинка')
        return 'Некорректный формат файла'

    try:
        picture_path: str = '/' + save_picture(picture)
    except FileNotFoundError:
        logging.error('Не найден файл')
        return 'Не найден файл'
    except JSONDecodeError:
        return 'Некорректный файл'

    post = add_post({'pic': picture_path, 'content': content})
    return render_template('post_uploaded.html', post=post)