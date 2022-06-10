"""Movies app URL config"""

from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'directors', views.DirectorViewSet)


app_name = 'movies'
urlpatterns = router.urls
