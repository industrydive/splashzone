import os.path
from django import template

register = template.Library()


@register.filter(name='pdb')
def pdb(item, item2=None):
    import pdb  # noqa
    pdb.set_trace()  # noqa


@register.filter(name='story_image')
def story_image(story):
    image_path = 'static/image/news/{}.jpg'.format(story.pk)
    if os.path.exists(image_path):
        return 'image/news/{}.jpg'.format(story.pk)
    return 'image/placeholder-img.jpg'