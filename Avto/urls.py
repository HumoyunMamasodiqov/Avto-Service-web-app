from django.urls import path
from .views import home, usta_filter, usta_profile, seting, user_profile, all_masters, splash, evukator, my_avto
urlpatterns = [
    path('', splash, name='splash'),
    path("home/", home, name="home"),
    path('usta-filter/', usta_filter, name='usta_filter'),
    path('ustalar/<int:usta_id>/', usta_profile, name='usta_profile'),
    path("seting/", seting, name="seting"),
    path("user_profile", user_profile, name="user_parofile"),
    path("all_master", all_masters, name="all_master"),
    path("evukator", evukator, name="evukator"),
    path("my_avto", my_avto, name="my_avto"),
]
