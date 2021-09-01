from django.template import loader
from django.http import HttpResponse
from django.views import View

from wavepool.onboarding_exercise_defs import prompts


def instructions(request):
    template = loader.get_template('instructions2.html')

    context = {
        'prompts': prompts,
        'spoonser': None,
        'show_topics': False,
        'show_footer_signup': False,
    }
    return HttpResponse(template.render(context, request))


class Signup(View):
    def setup(self, request, *args, **kwargs):
        super(Signup, self).setup(request, *args, **kwargs)
        self.template = loader.get_template('thankyou.html')
        self.context = {
            'spoonser': None,
            'show_topics': False,
            'show_footer_signup': False,
        }

    def get(self, request, *args, **kwargs):
        return HttpResponse(self.template.render(self.context, request))

    def post(self, request, *args, **kwargs):
        return HttpResponse(self.template.render(self.context, request))
