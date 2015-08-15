from django.contrib import admin

# Register your models here.
from .models import Question, Answer

class AnswerInline(admin.StackedInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [AnswerInline]


admin.site.register(Question, QuestionAdmin)

