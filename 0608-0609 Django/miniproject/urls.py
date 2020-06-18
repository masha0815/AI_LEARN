

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.index),
    path('topic/', topic.views.index)
    path('topiz/add_topic/', topic.views.add_topic),
    path('content/', content.views.index)
]




