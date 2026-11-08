from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('keepsimple/', TemplateView.as_view(
        template_name='keepsimple/index.html')),

    path('keepsimple/index.html', TemplateView.as_view(
        template_name='keepsimple/index.html')),

    path('keepsimple/demo.html', TemplateView.as_view(
        template_name='keepsimple/demo.html')),

    path('keepsimple/archives.html', TemplateView.as_view(
        template_name='keepsimple/archives.html')),

    path('keepsimple/blog.html', TemplateView.as_view(
        template_name='keepsimple/blog.html')),

    path('keepsimple/single.html', TemplateView.as_view(
        template_name='keepsimple/single.html')),

    path('keepsimple/page.html', TemplateView.as_view(
        template_name='keepsimple/page.html')),

    path('blog/', include('blogapp.urls')),
    path('eventassistant/', include('eventassistant.urls')),
    path('', include('bassroom.urls')),
]