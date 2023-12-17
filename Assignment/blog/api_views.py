# from django.shortcuts import render
# from models import blogdata


# # Create your views here.
# def BlogView(request):
#     blogs=blogdata.objects.all()
#     output={
#         "blogs":blogs
#     }

# api_views.py

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Blog
import json
from django.views.decorators.csrf import csrf_exempt

# from .forms import BlogForm


@csrf_exempt
def BlogAPIView(request, id=None):
	output = {"data": None}
	method = request.method

	if method == "GET":
		print("doing get..")
		if id is None:
			blog = list(Blog.objects.all().values('id','title','category','description'))
			output['data'] = blog
		else:
			blog = Blog.objects.get(id=id)
			output['data'] = {
				'id': id,
				'title': blog.title,
				'category':blog.category,
				'description':blog.description
			}

	elif method == "POST":
		print("doing post..")
		print("raw data : ", request.body)
		data = json.loads(request.body)
		print("Json converted data : ", data)

		data_post = {
			'title': data['title'],
			'description': data['description'],
			'category' :data['category'],
			
		}
		
		output['data']=data_post
		c = Blog(**data_post)
		c.save()
		


	elif method == "PATCH":
		print("doing patch..")
		data = json.loads(request.body)
		c = Blog.objects.filter(id=id)
		
		data_to_update = {}
		fields = ['title', 'description', 'category']
		
		for field in fields:
			if data.get(field):
				data_to_update[field] = data.get(field)
		output['data']=data_to_update
		c.update(**data_to_update)


	elif method == "DELETE":
		print("doing delete..")
		c = Blog.objects.filter(id=id)
		
		c.delete()
	return JsonResponse(output)



# def post_blog(request):

#     if request.method == 'POST':
#         form = BlogForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return JsonResponse({'message': 'Blog created successfully'})
#     else:
#         form = BlogForm()
#     return render(request, 'post_blog.html', {'form': form})

# def update_blog(request, blog_id):
#     blog = get_object_or_404(Blog, id=blog_id)
#     if request.method == 'POST':
#         form = BlogForm(request.POST, instance=blog)
#         if form.is_valid():
#             form.save()
#             return JsonResponse({'message': 'Blog updated successfully'})
#     else:
#         form = BlogForm(instance=blog)
#     return render(request, 'update_blog.html', {'form': form})
