from django.contrib import admin

from to_do_list.models import Task
# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'status', 'due_date']
    list_filter = ['status']
    search_fields = ['status', 'id']
    fields = ['id', 'content', 'status', 'due_date']
    readonly_fields = ['due_date']

admin.site.register(Task, TaskAdmin)
