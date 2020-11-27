from django.contrib import admin

# Register your models here.
from . models import *

admin.site.register(BOOK)
admin.site.register(STAFF)
admin.site.register(USER)
admin.site.register(LIBRARIAN)
admin.site.register(PUBLISHER)
admin.site.register(AUTHOR)
admin.site.register(STOCK)
admin.site.register(BORROWEDBOOK)
admin.site.register(WRITTENBY)
