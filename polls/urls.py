from django.conf.urls import patterns, include, url

from polls import views

urlpatterns=patterns('',
		

		# for custom view
		#url(r'^$',views.index,name='index'),
		#url(r'^(?P<question_id>\d+)/$',views.detail,name='detail'),
		#url(r'^(?P<question_id>\d+)/results/$',views.results,name='results'),

		# for generic view
		url(r'^$',views.IndexView.as_view(),name='index'),
		url(r'^(?P<pk>\d+)/$',views.DetailView.as_view(),name='detail'),          # pkas primary key
		url(r'^(?P<pk>\d+)/results/$',views.ResultsView.as_view(),name='results'),
		url(r'^(?P<question_id>\d+)/vote/$',views.votes,name='votes'),

	)
