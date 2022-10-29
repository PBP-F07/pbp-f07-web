from django.urls import path
from keuangan.views import *

app_name = 'keuangan'

urlpatterns = [
    path('', show_keuangan, name='show_keuangan'),
    path('admin/', show_admin, name='show_admin'),
    path('user/', show_user, name='show_user'),
    path('user/create-cashout/', user_create_cashout, name='user_create_cashout'),
    path('json/user/', user_get_keuangan_data_json, name='user_get_keuangan_data_json'),
    path('json/user-cashouts/', user_get_all_cashouts_json, name='user_get_all_cashouts_json'),
]