from django.contrib import admin

from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("product", "created_by", "rating", "content", "created_at")


admin.site.register(Review, ReviewAdmin)
