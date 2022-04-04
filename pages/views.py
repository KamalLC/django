from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import HomePage, Blog
from .forms import BlogForm,BlogModelForm
from django.urls import reverse_lazy

#Class Based Views (Base View)
from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

#Class Based Views (Generic View)
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

# Create your views here.

def index(request):
    # homepage_data = HomePage.objects.all()
    # print(homepage_data)
    # print(type(homepage_data))
    homepage_data = HomePage.objects.get(id=1)
    context = {
        'title':homepage_data.title,
        'para1':homepage_data.para1,
        'para2':homepage_data.para2,
        'skills_list':homepage_data.skills_list,
        'softwares_list':homepage_data.softwares_list,
        'mail':homepage_data.mail,
        
    }
    return render(request, "pages/index.html",context)

def contact(request):
    #return HttpResponse("Hello, world. You're at the portfolio contact.")
    return render(request, "pages/contact.html")

def blog(request):
    blogs_list = Blog.objects.all()
    print(blogs_list)
    
    context = {
        'blogs_list':blogs_list,
    }
    
    return render(request, "blogs/blogs.html",context)

def blog_detail(request,id):
    blog = Blog.objects.get(id=id)
    context = {
        'blog': blog
    }
    return render(request, "blogs/blog_detail.html",context)


def blog_create(request):
    if request.method == 'POST':
        form = BlogModelForm(request.POST,request.FILES)
        if form.is_valid():
            # # do something useful
            # print('form is valid')
            # print(form.cleaned_data)
            # print('Title:', form.cleaned_data['title'])
            # print('Paragraph:', form.cleaned_data['paragraph'])
            # return HttpResponse('success')
            Blog.objects.create(**form.cleaned_data)
            #form.save()
            return redirect('/blog')
        else:
             print('form is not valid')
             print(form.errors)
             return HttpResponse('error')
    else:
        form = BlogModelForm()

    return render(request, 'blogs/blog_create.html', {'form': form})

def blog_update(request,id):
    blog = Blog.objects.get(id=id)
    print(blog.title)
    if request.method == 'POST':
        form = BlogModelForm(request.POST,request.FILES,instance=blog)
        if form.is_valid():
            #Blog.objects.filter(id=id).update(**form.cleaned_data)
            form.save()
            #return redirect('/blog')
            return redirect('/blog_detail/'+str(form.instance.id))
        else:
            print('form is not valid')
            print(form.errors)
            return HttpResponse('error')
    else:
        form = BlogModelForm(instance=blog)
    return render(request, 'blogs/blog_update.html', {'form': form})



#delete blog
def blog_delete(request,id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect('/blog')



#1
class Index(TemplateView):
    template_name = 'pages/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        homepage_data = HomePage.objects.get(id=1)
        context = {
        'title':homepage_data.title,
        'para1':homepage_data.para1,
        'para2':homepage_data.para2,
        'skills_list':homepage_data.skills_list,
        'softwares_list':homepage_data.softwares_list,
        'mail':homepage_data.mail,
        }
        return context

    

#3
class BlogList(ListView):
    model = Blog
    template_name=  'blogs/blogs.html'
    context_object_name = 'blogs_list'

#5 
class BlogDetail(DetailView):
    model = Blog
    template_name=  'blogs/blog_detail.html'
    context_object_name = 'blog'


class MyBlogDetail(LoginRequiredMixin,UserPassesTestMixin,DetailView):
    login_url = '/signin/'
    model = Blog
    template_name=  'blogs/myblog_detail.html'
    context_object_name = 'blog'
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user     

#7
class BlogCreate(CreateView):
    model = Blog
    form_class = BlogModelForm
    template_name = 'blogs/blog_create.html'
    success_url = '/blog'
    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)

#9
class BlogUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    login_url = '/signin/'
    model = Blog
    #form_class = BlogModelForm
    fields = ['title','subtitle', 'paragraph','image'] 
    template_name = 'blogs/blog_update.html'
    #11 changes to model to get absolute url
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user     

#12
class BlogDelete(LoginRequiredMixin,UserPassesTestMixin,DeleteView): 
    login_url = '/signin/'
    model = Blog
    template_name = 'blogs/blog_delete.html'
    success_url = reverse_lazy('blog')   

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user  




class MyBlogList(LoginRequiredMixin,ListView):
    login_url = '/signin/'
    model = Blog
    template_name=  'blogs/myblogs.html'
    context_object_name = 'blogs_list'

    def get_queryset(self):
        user = self.request.user
        return Blog.objects.filter(author=user)