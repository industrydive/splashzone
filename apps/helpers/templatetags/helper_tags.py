import os.path
from django import template

register = template.Library()


@register.filter(name='pdb')
def pdb(item, item2=None):
    import pdb  # noqa
    pdb.set_trace()  # noqa


@register.filter(name='story_image')
def story_image(story):
    if story:
        image_path = 'static/image/news/{}.jpg'.format(story.pk)
        if os.path.exists(image_path):
            return 'image/news/{}.jpg'.format(story.pk)
    return 'image/placeholder-img.jpg'


@register.filter(name='gherkinize_step')
def gherkinize_step(step):
    gherkin_starters = [
        'Given', 'When', 'Then', 'And'
    ]
    split_str = step.split(' ')
    if split_str[0] in gherkin_starters:
        split_str[0] = '<strong>{}</strong>'.format(split_str[0])
        return ' '.join(split_str)
    if '<table>' in step:
        return '<code>{}</code>'.format(step)
    return step
