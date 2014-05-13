from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'diloo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','app.views.main', name="main"),
    url(r'^feed$','app.views.feed', name="feed"),
    url(r'^login$', 'app.views.login', name="login"),
    url(r'^register$', 'app.views.register', name="register"),
    url(r'^logout$', 'app.views.logout', name="logout"),
    url(r'^profile/(?P<username>\w+)$', 'app.views.profile', name="profile"),
    url(r'^p/(?P<username>\w+)$', 'app.views.profile', name="short_profile"),
    url(r'^u$', 'app.views.user_profile', name="user_profile"),
    url(r'^u/edit$', 'app.views.user_profile_configuration', name="user_profile_configuration"),
    url(r'^s$', 'app.views.search', name="search_short"),
    url(r'^search$', 'app.views.search', name="search"),
    url(r'^d/(?P<number>\d+)$', 'app.views.review', name="review"),
    url(r'^r/u$', 'app.views.review_upload', name="review_upload"),
    url(r'^r/h$', 'app.views.review_heart', name="review_heart"),
    url(r'^r/h/d$', 'app.views.review_heart_delete', name="review_heart_delete"),
    url(r'^ur$', 'app.views.ur', name="ur"),
)

