from django import forms
from django.contrib import admin, messages
from news.models import NewsPost


class NewsPostForm(forms.ModelForm):
    model = NewsPost
    fields = '__all__'


class NewsPostAdmin(admin.ModelAdmin):
    form = NewsPostForm
    list_display = ['title', 'source_divesite', 'is_cover_story', 'active']
    list_editable = ['is_cover_story', 'active']

    """
    message_user is used to bypass the default message response with a custom one
    """
    def message_user(self, request, message, level=messages.INFO, extra_tags='', fail_silently=True):
        pass

    """
     save_model saves the object changes but also notifies 
     the user when the button submitted no cover story. Last,
     it will force the user to choose only one cover story.

     :param self: NewsPostAdmin
     :param request: HTTP POST request
     :param object: NewsPost
     :return: none
     """
    def save_model(self, request, obj, form, change):
        super(NewsPostAdmin, self).save_model(request, obj, form, change)
        if change:
            if obj.is_cover_story:
                NewsPost.objects.filter(is_cover_story=True).update(is_cover_story=False)
                obj.save()
            if not obj.is_cover_story:
                messages.error(request, 'WARNING! There is no cover story!')



admin.site.register(NewsPost, NewsPostAdmin)
