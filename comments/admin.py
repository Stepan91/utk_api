from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('pub_date',)
    list_display = ('phone', 'email', 'comment')
    search_fields = ('phone', 'email')


admin.site.register(Comment, CommentAdmin)
