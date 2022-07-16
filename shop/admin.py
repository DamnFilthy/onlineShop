from django.contrib import admin
from .models import User, Gadget, Category, GadgetImage

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'updated_at')


class GadgetImageInline(admin.TabularInline):
    model = GadgetImage


@admin.register(Gadget)
class GadgetAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'created_at', 'updated_at')
    inlines = [GadgetImageInline, ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
