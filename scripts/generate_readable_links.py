from index.helpers import remove_special_chars
from index.models import post

def run():
    posts = post.objects.all()
    for post_entry in posts:
        link = post_entry.head.replace(" ", "-")
        post_entry.link = remove_special_chars(link).lower()
        post_entry.save()