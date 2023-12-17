from django.shortcuts import render
from models import Blog


# # # Create your views here.
def BlogView(request):
    blogs=Blog.objects.all()
    output={
        "blogs":blogs
    }


# # views.py
# from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import render, get_object_or_404
# from django.http import JsonResponse
# from .models import Blog
# # from .forms import BlogForm
# def get_all_blogs(request):
#     blogs = Blog.objects.all()
#     data = [{'title': blog.title, 'description': blog.description, 'category': blog.category} for blog in blogs]
#     print("hellooooooooooo.....................")
#     return JsonResponse(data, safe=False)

# # def get_blog_by_id(request, blog_id):
# #     blog = get_object_or_404(Blog, id=blog_id)
# #     data = {'title': blog.title, 'description': blog.description, 'category': blog.category}
# #     return JsonResponse(data)

# # def post_blog(request):
# #     if request.method == 'POST':
# #         form = BlogForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             return JsonResponse({'message': 'Blog created successfully'})
# #     else:
# #         form = BlogForm()
# #     return render(request, 'post_blog.html', {'form': form})

# # def update_blog(request, blog_id):
# #     blog = get_object_or_404(Blog, id=blog_id)
# #     if request.method == 'POST':
# #         form = BlogForm(request.POST, instance=blog)
# #         if form.is_valid():
# #             form.save()
# #             return JsonResponse({'message': 'Blog updated successfully'})
# #     else:
# #         form = BlogForm(instance=blog)
# #     return render(request, 'update_blog.html', {'form': form})
