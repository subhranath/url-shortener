from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from url_shortify import utils
from url_shortify.forms import URLShortifyForm

def index(request):
    """Index view handler.
    """
    shortify = None
    if request.method == 'GET':
        form = URLShortifyForm()
    else:
        form = URLShortifyForm(request.POST)
        if form.is_valid():
            shortify = utils.shortify(request, form.cleaned_data)
            if shortify:
                messages.add_message(request, messages.SUCCESS, \
                                     'Successfully shortified')                
            else:
                messages.add_message(request, messages.ERROR, \
                                     'Unexpected error')
    return render_to_response('url_shortify/index.html', { \
        'form': form, \
        'shortify': shortify, \
    }, context_instance=RequestContext(request))
    