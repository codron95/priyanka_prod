from django.shortcuts import render,get_object_or_404
from priyanka.settings import MEDIA_URL
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import post,photo,comment,subscribers,comment_photo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json

# Create your views here.
def index(request):
	context={'MEDIA_URL':MEDIA_URL}
	return render(request,"index.html",context)

@csrf_exempt
def subscribe(request):
	email=request.POST['email']
	subscriber=subscribers.objects.filter(email=email)
	if subscriber:
		return HttpResponse("Already Subscribed.!")
	else:
		subscriber=subscribers(email=email)
		subscriber.save()
		return HttpResponse("You are awesome.!")

def scrible(request,type,id=-1):
	bg="sto_bg.jpg";
	if type=="stories":
		bg="sto_bg.jpg";
	elif type=="travelogues":
		bg="tra_bg.jpg";
	elif type=="published":
		bg="pub_bg.jpg";

	if id==-1:
		posts=post.objects.filter(post_type=type.strip()).order_by('-created_date')
		current_post=posts[0]
	else:
		current_post=get_object_or_404(post,id=id,post_type=type.strip())

	if request.method=="POST":
		new_comment=comment(name=request.POST['name'],content=request.POST['content'],post=current_post,email=request.POST['email'])
		new_comment.save()

	try:
		next_post=current_post.get_next_by_created_date(post_type=type.strip())
	except post.DoesNotExist:
		next_post=-1
	
	try:
		prev_post=current_post.get_previous_by_created_date(post_type=type.strip())
	except post.DoesNotExist:
		prev_post=-1



	try:
		comments=current_post.comment_set.all().order_by('-created_date')
	except:
		comments=-1

	paginator = Paginator(comments, 10)
	page = request.GET.get('page')
	try:
		comment_page = paginator.page(page)
	except PageNotAnInteger:
		comment_page = paginator.page(1)
	except EmptyPage:
		comment_page = paginator.page(paginator.num_pages)

	recents=post.objects.filter(post_type=type.strip()).order_by('-created_date')[:5]

	context={'current':current_post,
			'next_post':next_post,
			'prev_post':prev_post,
			'hid':'hide','type':type,
			'recents':recents,
			'comments':comment_page,
			'url':request.path,
			'bg':bg,}
	return render(request,"scrible.html",context)

def clicks(request,type):
	photos=photo.objects.filter(photo_type=type)
	context={'MEDIA_URL':MEDIA_URL,'type':type,'photos':photos}
	return render(request,"clicks.html",context)

def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

@csrf_exempt
def return_comments(request):
	name=[]
	content=[]
	created_date=[]
	id=request.POST.get('id')
	num_comments=request.POST.get('num');
	print(num_comments)
	current_photo=photo.objects.filter(id=id)
	try:
		comments=current_photo[0].comment_photo_set.all().order_by('-created_date')[:int(num_comments)]
		print(len(comments));
		if len(comments)<int(num_comments):
			view_more_flag=0;
		else:
			view_more_flag=1;
		
	except:
		comments=-1
		view_more_flag=0;

	for result in comments:
		name.append(result.name)
		content.append(result.content)
		created_date.append(result.created_date)


	return HttpResponse(json.dumps({'name':name,'content':content,'created_date':created_date,'flag':view_more_flag},default=date_handler))

@csrf_exempt
def create_comment(request):
	id=request.POST.get("id")
	current_photo=photo.objects.filter(id=id)
	new_comment=comment_photo(name=request.POST['name'],content=request.POST['content'],photo=current_photo[0],email=request.POST['email'])
	new_comment.save()
	return HttpResponse("done")

def contact(request):
	return render(request,"contact.html")


