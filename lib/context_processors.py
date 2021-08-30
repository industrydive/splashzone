from lib.sitestuff import current_site


def site_processor(request):
    this_site = current_site()
    return {
        'site': this_site
    }
