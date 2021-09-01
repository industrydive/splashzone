from lib.sitestuff import current_site

from advertising import get_ad


def site_processor(request):
    this_site = current_site()
    request.site = this_site
    return {
        'site': this_site,
        'show_topics': True,
    }


def ads_processor(request):
    return {
        'spoonser': get_ad()
    }
