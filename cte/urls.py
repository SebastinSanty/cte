from django.conf.urls import include, url
from django.contrib import admin
from home.forms import EmailDomainFilterRegistrationForm
from registration.backends.default.views import RegistrationView

urlpatterns = [
    # Examples:
    url(r'^$', 'home.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^register/$',
    RegistrationView.as_view(form_class=EmailDomainFilterRegistrationForm),
    name='registration_register'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^courses/$', 'course.views.Courses', name='courses'),
    url(r'^dashboard/', 'home.views.dashboard', name='dashboard') 
]
