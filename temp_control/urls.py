from django.urls import path
from temp_control import views
from django.views.generic import RedirectView

app_name = 'temp_control'

urlpatterns = [
    path('', RedirectView.as_view(url='/temp-control/')),
    # views for template
    path('temp-control/', views.index, name='room_info'),
    path('temp-control/cooler/toggle/',views.cooler_toggle ,name="cooler_toggle"),
    path('temp-control/heater/toggle/',views.heater_toggle ,name="heater_toggle"),
    path('temp-control/mode/toggle/',views.automatic_toggle ,name="automatic_toggle"),
    #views for API,
    path("api/temp-control/", views.room_info),
    path("api/temp-control/cooler/toggle/", views.cooler_toggle_API),
    path("api/temp-control/heater/toggle/", views.heater_toggle_API),
    path("api/temp-control/mode/toggle/", views.automatic_toggle_API),

]
