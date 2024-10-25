from django.shortcuts import render, get_object_or_404
from blog.models import BlogTable
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, Page

# Create your views here.
def blog_list_view(request):
    post_list = BlogTable.objects.all() 

    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page')
    try:
        post_list = paginator.page(page_number)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    print(post_list)
    print(type(post_list))
    print(str(post_list))

    dict_data = {
        'page_list' : post_list
    }
    response = render(request, 'blog/home.html', context=dict_data)
    return response

def blog_details_view(request, slug):
    blog_details = get_object_or_404(BlogTable, slug=slug)
    # blog_details = BlogTable.objects.get(slug = urllink)
    print("This is data ", blog_details)
    print(type(blog_details))
    dict_data = {
        'blog_details' : blog_details,
    }
    response = render(request, 'blog/blog_details.html', context=dict_data)
    return response
