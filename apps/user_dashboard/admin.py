from django.contrib import admin
from django.conf.urls import url, include


from models import User, Message, Comment

class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)

class MessageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Message, MessageAdmin)

class CommentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Comment, CommentAdmin)
