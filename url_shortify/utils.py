from url_shortify.models import URL

def shortify(request, form_cleaned_data):
    """Creates and returns a shortified url.
    """
    url = form_cleaned_data['url']
    shortified = URL.objects.create(request=request, original_url=url)
    return shortified
