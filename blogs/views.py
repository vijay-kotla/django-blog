from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from blogs.models import Blog, Category

# Create your views here.

def category_by_id(request, category_id):
    posts = Blog.objects.filter(status = 'Published', category_id=category_id)

    # use try-except to handle the case where the category does not exist
    # try:
    #     category = Category.objects.get(id=category_id)
    # except:
    #     return redirect('home')  # Redirect to home if category does not exist
    
    # use get_object_or_404 to retrieve the category object, which will raise a 404 error if the category does not exist
    category =  get_object_or_404(Category, id=category_id)
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)