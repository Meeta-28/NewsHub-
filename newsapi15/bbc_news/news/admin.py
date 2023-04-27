from django.contrib import admin
from .models import Article
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .forms import UserRegisterForm

from django.contrib.auth.admin import UserChangeForm

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'img_url', 'source_url', 'source_name', 'created_at', 'summary')

class CustomUserAdmin(UserAdmin):
    add_form = UserRegisterForm
    form = UserChangeForm
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'date_joined', 'last_login')
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

'''from django.contrib import admin
from .models import Article
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserChangeForm

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'img_url', 'source_url', 'source_name', 'created_at', 'summary')

class CustomUserAdmin(UserAdmin):
    add_form = UserRegisterForm
    form = UserChangeForm
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'date_joined', 'last_login')
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)'''










# Register your models here.
