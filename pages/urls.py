from django.urls import path

from .views import contact, index,blog,blog_detail,blog_create,blog_update,blog_delete,Index,BlogList,BlogDetail,BlogCreate,BlogUpdate,BlogDelete,MyBlogList,MyBlogDetail


urlpatterns = [
    #path("", index, name="index"),
    path("", Index.as_view(), name="index"), #2
    path("contact/", contact, name="contact"),
    #path("blog/", blog, name="blog"),
    path("blog/", BlogList.as_view(), name="blog"),  #4
    path("myblog/", MyBlogList.as_view(), name="myblog"),
    #path('blog_detail/<int:id>', blog_detail, name="blog_detail"),
    path('blog_detail/<int:pk>', BlogDetail.as_view(), name="blog_detail"), #6
    path('myblog_detail/<int:pk>', MyBlogDetail.as_view(), name="myblog_detail"), #6
    #path('blog_create/', blog_create, name="blog_create"),
    path('blog_create/', BlogCreate.as_view(), name="blog_create"), #8
    #path('blog_update/<int:id>', blog_update, name="blog_update"), 
    path('blog_update/<int:pk>', BlogUpdate.as_view(), name="blog_update"), #10
    #path('blog_delete/<int:id>', blog_delete, name="blog_delete"),
    path('blog_delete/<int:pk>', BlogDelete.as_view(), name="blog_delete"),  #13
]