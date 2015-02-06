from django.contrib import admin


from polls.models import Question,Choice
# Register your models here.


class ChoiceInline(admin.TabularInline):
	model=Choice
	extra=3


class ChoiceAdmin(admin.ModelAdmin):
	model=Choice
	list_display=('choice_text','votes')


class QuestionAdmin(admin.ModelAdmin):
	#fields=['pub_date','question_text']
	fieldsets=[
		('Question',{'fields': ['question_text']}),
		('Data Information' , {'fields':['pub_date'],'classes':['collapse']}),
		]
	inlines=[ChoiceInline]
	# add filtering
	list_filter=['pub_date']
	search_fields=['question_text']
	list_display=('question_text','pub_date','was_published_recently')

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin)