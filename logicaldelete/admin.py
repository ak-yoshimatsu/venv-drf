import datetime

from django.contrib import admin

from logicaldelete.models import Event


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = "name", "deleted_at"
    actions = ["mark_as_deleted", "restore_records"]
    list_per_page = 10
    search_fields = ("name",)

    def get_queryset(self, request):
        return Event.all_objects.all()

    def mark_as_deleted(self, request, queryset):
        queryset.update(deleted_at=datetime.datetime.now())

    mark_as_deleted.short_description = "選択したレコードを論理削除"

    def restore_records(self, request, queryset):
        queryset.update(deleted_at=None)

    restore_records.short_description = "選択したレコードを復元"


admin.site.register(Event, EventAdmin)
