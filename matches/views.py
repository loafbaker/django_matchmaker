from django.shortcuts import render
from django.http import Http404

# Create your views here.
from jobs.models import Job, Location, Employer

def position_match_view(request, slug):
	try:
		instance = Job.objects.get(slug=slug)
	except Job.MultipleObjectsReturned:
		queryset = Job.objects.filter(slug=slug).order_by('-id')
		instance = queryset[0]
	except Job.DoesNotExist:
		raise Http404
	template = 'matches/position_match_view.html'
	context = {
		'instance': instance,
	}
	return render(request, template, context)
