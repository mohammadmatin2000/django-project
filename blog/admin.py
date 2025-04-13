from django.contrib import admin
from blog.models import Post,Category

# ======================================================================================================================
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','status','published_date','created_date','updated_date')
    list_filter = ('author','status','published_date','created_date','updated_date')
    search_fields = ('title','content')
    empty_value_display = '-empty-'
# ======================================================================================================================
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
# ======================================================================================================================