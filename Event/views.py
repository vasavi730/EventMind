from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from Event.models import DashBoard, queries
from rest_framework import viewsets
from .serializers import RecordSerializer
from django.core import mail
from django.utils.html import strip_tags
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
import uuid
import datetime
class DashViewSet(viewsets.ModelViewSet):
	queryset = DashBoard.objects.all()
	serializer_class = RecordSerializer
	def retrieve(self, request, *args, **kwargs):
		params = kwargs
		print(params['pk'])
		names = DashBoard.objects.filter(client_id=params['pk'])
		serializer = RecordSerializer(names,many=True)
		return Response(serializer.data)
@csrf_exempt
def update(request):
	name = request.POST.get("name")
	email = request.POST.get("email")
	address = request.POST.get("add")
	mob = request.POST.get("mob")
	event = request.POST.get("events")
	id1 = uuid.uuid4()
	date = datetime.datetime.now()
	obj = DashBoard(client_name=name,client_mobile=mob,client_address=address,client_event=event,client_status='Pending',client_email=email,client_id=id1)
	obj.save()
	ctx={
		'event':event,
		'id1':id1,
		'address':address
	}
	touser = str(email)
	efrom = settings.EMAIL_HOST_USER
	sub = 'Your request is received'
	reclist = [touser]
	html_message = get_template('confirm.html').render(ctx)
	plain_message = strip_tags(html_message)
	msg = EmailMessage(
		sub,
		html_message,
		efrom,
		reclist
	)
	msg.content_subtype="html"
	msg.send()
	return render(request,'recieved.html')

def accepted(request):
	obj = DashBoard.objects.filter(client_status='Accepted')
	msg=''
	lst=[]
	for x in obj:
		w={
			'name' : x.client_name,
			'number' : x.client_mobile,
			'address' : x.client_address,
			'Event' : x.client_event,
			'Email' : x.client_email,
			'Status' : x.client_status,
			'id' : x.client_id
		}
		lst.append(x)
	return render(request,'accepted_list.html',{'lst':lst})
@csrf_exempt
def admin_login(request):
	u = request.POST.get("u")
	p = request.POST.get("p")
	if u=='admin@eventmind' and p=='EventMind@intern':
		obj = DashBoard.objects.filter(client_status='Pending')
		msg=''
		lst=[]
		for x in obj:
			w={
				'name' : x.client_name,
				'number' : x.client_mobile,
				'address' : x.client_address,
				'Event' : x.client_event,
				'Email' : x.client_email,
				'Status' : x.client_status,
				'id' : x.client_id
			}
		lst.append(x)
		return render(request,'StatusBoard.html',{'lst':lst})
	else:
		return HttpResponse('Invalid username or password')
def rejected(request):
	obj = DashBoard.objects.filter(client_status='Declined')
	msg=''
	lst=[]
	for x in obj:
		w={
			'name' : x.client_name,
			'number' : x.client_mobile,
			'address' : x.client_address,
			'Event' : x.client_event,
			'Email' : x.client_email,
			'Status' : x.client_status,
			'id' : x.client_id
		}

		lst.append(x)

	return render(request,'rejected_list.html',{'lst':lst})

def pending(request):
	obj = DashBoard.objects.filter(client_status='Pending')
	msg=''
	lst=[]
	for x in obj:
		w={
			'name' : x.client_name,
			'number' : x.client_mobile,
			'address' : x.client_address,
			'Event' : x.client_event,
			'Email' : x.client_email,
			'Status' : x.client_status,
			'id' : x.client_id
		}

		lst.append(x)
	return render(request,'StatusBoard.html',{'lst':lst})

def accept(request, id1):
	obj = DashBoard.objects.filter(client_id=id1).update(client_status='Accepted')
	obj = DashBoard.objects.filter(client_id=id1)
	efrom = settings.EMAIL_HOST_USER
	sub = 'Your request is accepted'
	
	for x in obj:
		name = x.client_name
		email = x.client_email
	ctx = {
		'name': name,
		'id1':id1
	}	
	touser = str(email)
	reclist = [touser]
	html_message = get_template('accept.html').render(ctx)
	plain_message = strip_tags(html_message)
	msg = EmailMessage(
		sub,
		html_message,
		efrom,
		reclist
	)
	msg.content_subtype="html"
	msg.send()
	obj = DashBoard.objects.filter(client_status='Accepted')
	msg=''
	lst=[]
	for x in obj:
		w={
			'name' : x.client_name,
			'number' : x.client_mobile,
			'address' : x.client_address,
			'Event' : x.client_event,
			'Email' : x.client_email,
			'Status' : x.client_status,
			'id' : x.client_id
		}

		lst.append(x)
	return render(request,'accepted_list.html',{'lst':lst})

def decline(request, id1):
	obj = DashBoard.objects.filter(client_id=id1).update(client_status='Declined')
	obj = DashBoard.objects.filter(client_id=id1)
	
	efrom = settings.EMAIL_HOST_USER
	sub = 'Your request is accepted'
	
	for x in obj:
		name = x.client_name
		email = x.client_email
	ctx = {
		'name': name,
		'id1':id1
	}	
	touser = str(email)
	reclist = [touser]
	html_message = get_template('reject.html').render(ctx)
	plain_message = strip_tags(html_message)
	msg = EmailMessage(
		sub,
		html_message,
		efrom,
		reclist
	)
	msg.content_subtype="html"
	msg.send()
	obj = DashBoard.objects.filter(client_status='Declined')
	msg=''
	lst=[]
	for x in obj:
		w={
			'name' : x.client_name,
			'number' : x.client_mobile,
			'address' : x.client_address,
			'Event' : x.client_event,
			'Email' : x.client_email,
			'Status' : x.client_status,
			'id' : x.client_id
		}

		lst.append(x)

	return render(request,'rejected_list.html',{'lst':lst})

@csrf_exempt
def query(request):
	n = request.POST.get("n")
	e = request.POST.get("e")
	q = request.POST.get("q")
	obj = queries(name=n,email=e,query=q)
	obj.save()
	msg = '<h1>Thanks for contacting us..</h1><br>'
	msg+='<a href=/index/>Return back</a>'
	
	return HttpResponse(msg)

def query_list(request):
	obj = queries.objects.all()
	lst = []
	for i in obj:
		w={
			'n':i.name,
			'e':i.email,
			'q': i.query
		}

		lst.append(w)
	return render(request, 'query_list.html',{'lst':lst})

def StatusBoard(request):
	obj = DashBoard.objects.filter(client_status='Pending')
	msg=''
	lst=[]
	for x in obj:
		w={
			'name' : x.client_name,
			'number' : x.client_mobile,
			'address' : x.client_address,
			'Event' : x.client_event,
			'Email' : x.client_email,
			'Status' : x.client_status,
			'id' : x.client_id
		}

		lst.append(x)
	return render(request,'StatusBoard.html',{'lst':lst})

def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

def wedding(request):
	return render(request,'wedding.html')

def birthday(request):
	return render(request,'birthday.html')

def surprise(request):
	return render(request,'surprise.html')

def product(request):
	return render(request,'product.html')

def theme(request):
	return render(request,'theme.html')

def retirements(request):
	return render(request,'retirements.html')

def annual(request):
	return render(request,'annual.html')

def booking(request):
	return render(request,'booking.html')

def login(request):
	return render(request,'login.html')

def accepted_list(request):
	return render(request,'accepted_list.html')

def rejected_list(request):
	return render(request,'rejected_list')

def pending_list(request):
	return render(request,'pending_list.html')

def about(request):
	return render(request,'about.html')

def contact(request):
	return render(request,'contact.html')

def gallery(request):
	return render(request,'gallery.html')

def received(request):
	return render(request,'recieved.html')
	
def confirm(request):
	return render(request,'confirm.html')
