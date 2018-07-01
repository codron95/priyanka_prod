from index.helpers import generate_link
from index.models import post

def run():
    posts = post.objects.all()
    for post_entry in posts:
        post_entry.link = generate_link(post_entry.head)
        post_entry.save()