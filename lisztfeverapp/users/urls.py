from django.conf.urls import url
from django.urls import include, path  #django 2.0 version url dispatcher
from . import views

app_name = "users"
urlpatterns = [
    path("", view=views.UserMain.as_view(), name='main'),
    path("plans/", view = views.UserPlan.as_view(), name = 'user_plans'),
    path("settings/", view = views.UserSetting.as_view(), name = 'user_events'),
    path('login/facebook/', view=views.FacebookLogin.as_view(), name='fb_login'),
    path("signed_request/", view=views.FacebookSignedRequest.as_view(), name='signed_request')
]
