from django.contrib import admin

from .models import (   User,
                        user1,
                        admin1,
                        meeting, 
                        org,  
                        usereg )

# Register your models here.
admin.site.register(User)
admin.site.register(user1)
admin.site.register(admin1)
admin.site.register(org)
admin.site.register(meeting)
admin.site.register(usereg)
