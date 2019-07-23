from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'card_app'

urlpatterns = [
    path('', views.CardIndexView.as_view(), name='card_index'),
    path('recent/', views.CardTemplateView.as_view(), name='card_recent'),
    path('popular/', views.CardTemplateView.as_view(), name='card_popular'),
    path('post_tag/<str:tag>', views.CardPostTagView.as_view(), name='card_post_tag'),
    path('detail/<int:pk>', views.CardDetailView.as_view(), name='card_detail'),
    path('chemical_tag/<str:tag>/', views.CardChemicalTagView.as_view(), name='card_chemical_tag'),
    path('comment/<int:pk>/', views.CardCommentCreateView.as_view(), name='card_comment'),
    path('recomment/<int:pk>/<int:comment_pk>', views.CardReCommentCreateView.as_view(), name='card_recomment'),
]
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)