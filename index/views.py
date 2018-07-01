import json
from collections import OrderedDict

from django.shortcuts import render,get_object_or_404
from priyanka.settings import MEDIA_URL
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import post,photo,comment,subscribers,comment_photo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.timezone import datetime
from django.db.models import Q
from django.core.urlresolvers import reverse

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

def scrible(request,type,link=None):
	bg="sto_bg.jpg";
	if type=="stories":
		bg="sto_bg.jpg";
	elif type=="travelogues":
		bg="tra_bg.jpg";
	elif type=="published":
		bg="pub_bg.jpg";

	if link is None:
		posts=post.objects.filter(post_type=type.strip()).order_by('-selected_date')
		current_post=posts[0]
	else:
		current_post=get_object_or_404(post,link=link,post_type=type.strip())

	try:
		next_post=current_post.get_next_by_selected_date(post_type=type.strip())
	except post.DoesNotExist:
		next_post=-1
	
	try:
		prev_post=current_post.get_previous_by_selected_date(post_type=type.strip())
	except post.DoesNotExist:
		prev_post=-1

	recents=post.objects.filter(post_type=type.strip()).order_by('-selected_date')[:5]
	posts_all=post.objects.filter(post_type=type.strip()).order_by('-selected_date')

	months=('January',
		'February',
		'March',
		'April',
		'May',
		'June',
		'July',
		'August',
		'September',
		'October',
		'November',
		'December')

	year_group=OrderedDict()
	year_start=2014
	year_now=datetime.now().year
	for i in range(year_now, year_start, -1):
		temp = OrderedDict()
		for k in range(1,13):
			p=post.objects.filter(selected_date__year=i,selected_date__month=k)
			if p.count():
				temp[months[k-1]]=p
		if len(temp):
			year_group[i]=temp

	# calculate disqus properties
	page_relative_url = reverse("scrible-param", kwargs={
													"type":current_post.post_type,
													"link":current_post.link
												})
	disqus_page_identifier = request.build_absolute_uri(page_relative_url)
	disqus_post_identifier = page_relative_url


	context={'current':current_post,
			'next_post':next_post,
			'prev_post':prev_post,
			'hid':'hide','type':type,
			'recents':recents,
			'url':request.path,
			'bg':bg,
			'all':posts_all,
			'arc_data':year_group,
			'disqus_page_identifier': disqus_page_identifier,
			'disqus_post_identifier': disqus_post_identifier}
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

def search(request):
	search_string=request.GET.get("query","-1")
	recents=post.objects.all().order_by('-created_date')[:5]
	if search_string!="-1":
		results=post.objects.filter(Q(head__icontains=search_string)|Q(content__icontains=search_string))
		if not results:
			results=0
		else:
			paginator = Paginator(results, 10)
			page = request.GET.get('page')
			try:
				results_page = paginator.page(page)
			except PageNotAnInteger:
				results_page = paginator.page(1)
			except EmptyPage:
				results_page = paginator.page(paginator.num_pages)
	else:
		results=0
		search_string=""
	context={'recents':recents,
			'results':results_page,
			'search_string':search_string
	}

	return render(request,"search.html",context)

def test(request):
	year_group=[]
	year_start=2014
	year_now=datetime.now().year
	for i in range(year_start,year_now+1):
		for k in range(1,13):
			temp={}
			p=post.objects.filter(selected_date__year=i,selected_date__month=k)
			temp[str(k)]=p
		year_group.append(temp)

	print(year_group)
	return HttpResponse("Test page working"+str(''))
