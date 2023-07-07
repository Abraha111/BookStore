from django.urls import path, include
from api.views import BookViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'books', BookViewSet, basename='book')


urlpatterns = [
    # path('api/', include(router.urls)),
    # path('upload/', BookViewSet.as_view(), name='document-upload'),
    # path('upload/', BookListCreateAPIView.as_view())
    path('', include(router.urls)),
]

