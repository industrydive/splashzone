from django.template import loader
from django.http import HttpResponse

from wavepool.onboarding_exercise_defs import prompts


def instructions(request):
    template = loader.get_template('wavepool/instructions2.html')

    context = {
        'prompts': prompts,
        'spoonser': None,
        'show_topics': False,
    }
    return HttpResponse(template.render(context, request))
