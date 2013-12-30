from django.http import HttpResponse
from django.shortcuts import render
import datetime, json, pytz

from home.models import Menu, MenuItem, Widget, SliderItem, CalendarItem, Member, MemberList, ContactGroup, Subscriber
from home.forms import SubscriberForm, ContactMessageForm
from django.utils import timezone

def set_timezone(request):
	if request.method == 'POST':
		request.session['django_timezone'] = request.POST['timezone']
	elif request.method == 'GET' and request.GET.get('timezone'):
		request.session['django_timezone'] = request.GET.get('timezone')
	return render(request, 'home/timezone.html', {'timezones': pytz.common_timezones})

def index(request):
	context = {}
	context['top_menu'] =  Menu.objects.get(name="top")
	context['slider_items'] =  SliderItem.objects.all()
	context['calendar_items'] =  CalendarItem.objects.order_by('time').filter(time__gt=timezone.now())[:3]
	context['left_widget'] =  Widget.objects.get(name="left")
	context['right_widget'] =  Widget.objects.get(name="right")
	return render(request, 'home/index.html', context)

def about(request):
	context = {}
	context['top_menu'] =  Menu.objects.get(name="top")
	return render(request, 'home/about.html', context)

def events_all(request):
	context = {}
	context['top_menu'] =  Menu.objects.get(name="top")
	context['calendar_items'] =  CalendarItem.objects.order_by('time').filter(time__gt=timezone.now())[:3]
	return render(request, 'home/events.html', context)

def events_json(request):
	context = {}
	calendar_items = CalendarItem.objects.order_by('time').filter(time__gt=datetime.datetime.fromtimestamp(int(request.GET.get('start'))),time__lt=datetime.datetime.fromtimestamp(int(request.GET.get('end',''))))
	items = []
	for c in calendar_items:
		items.append(c.to_dict(request)) 
	return HttpResponse(json.dumps(items), mimetype='application/json')

def event(request, pk):
	context = {}
	context['top_menu'] =  Menu.objects.get(name="top")
	context['item'] = CalendarItem.objects.get(pk=pk)
	return render(request, 'home/event.html', context)

def contact(request):
	context = {}
	context['top_menu'] =  Menu.objects.get(name="top")
	context['contact_groups'] = ContactGroup.objects.all()
	if request.method == 'POST':
		form = ContactMessageForm(request.POST)
		if form.is_valid():
			form.save()
			context["submitted"] = True
			context["name"] = form.cleaned_data.get("name")
			context["group"] = str(form.cleaned_data.get("group"))
	else:
		form = ContactMessageForm()
	context["form"] = form
	return render(request, 'home/contact.html', context)

def subscribe(request):
	context = {}
	context['top_menu'] =  Menu.objects.get(name="top")
	if request.method == 'POST':
		form = SubscriberForm(request.POST)
		if form.is_valid():
			form.save()
			context["subscribed"] = True
			context["email"] = form.cleaned_data.get("email")
			context["name"] = form.cleaned_data.get("name")
	else:
		form = SubscriberForm(initial={'email': request.GET.get('email')})
	context["form"] = form
	return render(request, 'home/subscribe.html', context)

def members_by_name(request, list):
	context = {}
	members = MemberList.objects.get(name=list)
	context['top_menu'] =  Menu.objects.get(name="top")
	context['title'] = members.title
	context['member'] =  members.member.all()
	return render(request, 'home/members.html', context)

def members_by_year(request, year):
	context = {}
	context['top_menu'] =  Menu.objects.get(name="top")
	context['title'] = "Class of %s" % year
	context['member'] =  Member.objects.filter(year=year)
	return render(request, 'home/members.html', context)