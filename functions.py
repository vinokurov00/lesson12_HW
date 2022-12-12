import json

def load_posts() -> list[dict]:
    with open("posts.json", 'r', encoding='utf-8') as file:
        return json.load(file)



def get_posts_by_keyword(keyword):
    result = []
    for post in load_posts():
        if keyword.lower() in post['content'].lower():
            result.append(post)
    return result

