from flask import Blueprint, render_template, request
from functions import get_posts_by_keyword, load_posts

main_page_blueprint = Blueprint('main_page_blueprint', __name__, template_folder='templates')

@main_page_blueprint.route('/')
def main_page():
    return render_template('index.html')


search_page_blueprint = Blueprint('search_page_blueprint', __name__, template_folder='templates')


@search_page_blueprint.route('/search/')
def search_page():
    keyword = request.args.get('s', '')
    posts = get_posts_by_keyword(keyword)

    return render_template('post_list.html', posts=posts, keyword=keyword)