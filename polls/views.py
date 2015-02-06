from django.shortcuts import render,get_object_or_404
from polls.models import Question,Choice
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse 
from django.views import generic
# Create your views here.

# using generic views
class IndexView(generic.ListView):
	template_name='polls/index.html'
	context_object_name='latest_question_list'

	def get_queryset(self):
		"""Returning last five published questions"""
		return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model=Question
	template_name='polls/detail.html'

class ResultsView(generic.DetailView):
	model=Question
	template_name='polls/results.html'

# using custom methods

#def index(request):
#	latest_question_list=Question.objects.order_by('-pub_date')[:5]
#	output='<br>'.join([p.question_text for p in latest_question_list])
#	context={'latest_question_list':latest_question_list}
#	return render(request,'polls/index.html',context)

#def detail(request,question_id):
#	question=get_object_or_404(Question,pk=question_id)   # checkid question id is in Question model
#	#return HttpResponse('Detail : Question id => %s' % question_id)	
#	return render(request,'polls/detail.html',{'question':question})

#def results(request,question_id):
#	#response="you are looking at the result of question  %s" 
#	question=get_object_or_404(Question,pk=question_id)
#	#return HttpResponse(response % question_id)
#	return render(request,'polls/results.html',{
#		'question':question,
#		})

def votes(request,question_id):
	p=get_object_or_404(Question,pk=question_id)

	try:
		selected_choice=p.choice_set.get(pk=request.POST['choice'])
	except(KeyError,Choice.DoesNotExist):
		return render(request,'polls/detail.html',{
			'question':p,
			'error_message':"Select choice",
			})
	else:
		selected_choice.votes+=1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))