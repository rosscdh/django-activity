# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.humanize.templatetags.humanize import naturaltime

from jsonfield import JSONField

import datetime


def log_event(actor, verb, description, **kwargs):
    return Action.objects.create(actor=actor,
                                 verb=verb,
                                 description=description,
                                 data=kwargs)


def _datetime():
    return datetime.datetime.utcnow()


class Action(models.Model):
    """
    """
    actor = models.CharField(max_length=255)
    verb = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    timestamp = models.DateTimeField(default=_datetime)

    data = JSONField(default={})

    class Meta:
        ordering = ('-timestamp', )

    @property
    def timesince(self):
        return naturaltime(self.timestamp)

    def __unicode__(self):
        return u'{actor} {verb} {description} - {timesince} [{data}]'.format(actor=self.actor,
                                                                             verb=self.verb,
                                                                             description=self.description,
                                                                             timesince=self.timesince,
                                                                             data=self.data)
