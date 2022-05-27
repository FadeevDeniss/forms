import pytz

from datetime import datetime

from django.conf import settings
from django.db import models
from pytz.tzinfo import DstTzInfo

tz: DstTzInfo = pytz.timezone(settings.TIME_ZONE)
local = datetime.now(tz=tz)


class CustomForm(models.Model):
				form_id = models.AutoField(primary_key=True)
				form_title = models.CharField(max_length=100)
				created_at = models.DateTimeField(default=local)


class FormFields(models.Model):
				form_id = models.ForeignKey(
								to=CustomForm,
								on_delete=models.CASCADE
				)
				field_name = models.CharField(max_length=100)
				field_description = models.CharField(max_length=100)
				field_type = models.CharField(
								max_length=10,
								choices=[
												('0', 'Text'),
												('1', 'Textarea'),
												('2', 'Select')
								],
								null=True,
								default=None,
				)
				field_choices = models.CharField(max_length=100, null=True)
				created_at = models.DateTimeField(default=local)
