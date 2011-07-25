from django.db import models
from django.http import HttpRequest
import hashlib
import random

class URLManager(models.Manager):
    def _generate_short_string(self, url):
        """Generates and returns a unique short string for a provided URL.
        """
        generate = True
        while generate:
            short_string = hashlib.md5(str(random.random()) + url).hexdigest()[:6]
            
            # Check if an unique short string has actually been generated or not.
            if self.model.objects.filter(short_string=short_string).count() == 0:
                generate = False            
        return short_string
    
    def create(self, **kwargs):
        if 'request' in kwargs.keys():
            request = kwargs['request']
            del kwargs['request']
            if isinstance(request, HttpRequest):
                url = URL(**kwargs)
                url.source_ip = request.META['REMOTE_ADDR']
                short_string = self._generate_short_string(url.original_url)
                url.short_string = short_string
                url.save()
                return url
            else:
                raise TypeError("create() expects a keyword argument "
                                "'request' of type HttpRequest")
        else:
            raise TypeError("create() expects a keyword argument 'request'")

class URL(models.Model):
    """Class to store a shortened URL data.
    """
    original_url = models.URLField(max_length=2000, verify_exists=False)
    short_string = models.CharField(max_length=100, unique=True, \
        blank=False, null=False, db_index=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    source_ip = models.GenericIPAddressField(blank=False, null=False)
    count = models.PositiveIntegerField(default=0, null=False)
    
    objects = URLManager()
    
    def __unicode__(self):
        return unicode(self.short_string)
    