from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'post_app'

urlpatterns = [
    path('', views.PostIndexView.as_view(), name='post_index'),
    path('recent/', views.PostTemplateView.as_view(), name='post_recent'),
    path('popular/', views.PostTemplateView.as_view(), name='post_popular'),
    path('detail/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post_tag/<str:tag>/', views.PostTagView.as_view(), name='post_tag'),
    path('chemical_tag/<str:tag>/', views.PostChemicalTagView.as_view(), name='chemical_tag'),
    path('comment/<int:pk>/', views.PostCommentCreateView.as_view(), name='post_comment'),
    path('recomment/<int:pk>/<int:comment_pk>', views.PostReCommentCreateView.as_view(), name='post_recomment'),
]
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)