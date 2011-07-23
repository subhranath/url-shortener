from django.db import models

class URL(models.Model):
    """Class to store a shortened URL data.
    """
    original_url = models.URLField(max_length=2000, verify_exists=False)
    short_string = models.TextField(db_index=True, unique=True, \
                                    blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    source_ip = models.GenericIPAddressField(blank=False, null=False)
    count = models.PositiveIntegerField(default=0, null=False)
    
    def __unicode__(self):
        return unicode(self.short_string)
