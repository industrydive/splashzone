from django.template import loader
from django.http import HttpResponse

from wavepool.code_exercise_defs import code_prompts, code_reviews


def instructions(request):
    template = loader.get_template('wavepool/instructions.html')

    context = {
        'code_prompts': code_prompts,
        'code_reviews': code_reviews,
    }
    return HttpResponse(template.render(context, request))
