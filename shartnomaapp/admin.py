from typing import KeysView
from django.contrib import admin

from CRM.shartnomaapp.models import Kurs, Shartnoma, Student, Ustoz

# Register your models here.
admin.site.register(Shartnoma)
admin.site.register(Student)
admin.site.register(Ustoz)
admin.site.register(Kurs)