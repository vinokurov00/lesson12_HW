import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request
from functions import get_posts_by_keyword

main_page_blueprint = Blueprint('main_page_blueprint', __name__, template_folder='templates')
search_page_blueprint = Blueprint('search_page_blueprint', __name__, template_folder='templates')


@main_page_blueprint.route('/')
def main_page():
    return render_template('index.html')


@search_page_blueprint.route('/search/')
def search_page():
    keyword = request.args.get('s', '')
    logging.info('Выполняется поиск')
    try:
        posts = get_posts_by_keyword(keyword)
    except FileNotFoundError:
        return 'Не найден файл'
    except JSONDecodeError:
        return 'Некорректный файл'

    return render_template('post_list.html', posts=posts, keyword=keyword)