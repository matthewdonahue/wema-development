from django.contrib import admin
from members.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'gup_num')

    def user_info(self, obj):
        return obj.description

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('name')
        return queryset

admin.site.register(UserProfile, UserProfileAdmin)