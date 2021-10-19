from django.contrib import admin
from .models import Category, SubCategory, QuestionBank, Comment


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Comment)
admin.site.register(QuestionBank)
