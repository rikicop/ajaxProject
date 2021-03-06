from django.contrib import admin
from django.urls import path
#from pages.views import  home,SignUpView,validate_username,contact_form
from pages.views import contact_form,sum_form,download_file,edit_contact
#from my_app.views import (indexView,postFriend)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', home, name='home'),
    #path('signup', SignUpView.as_view(), name='signup'),
    #path('validate_username', validate_username, name='validate_username'),
    #path('', indexView),
    #path('post/ajax/friend', postFriend, name = "post_friend"),
    path('contact-form/', contact_form, name='contact_form'),
    path('edit-contact/', edit_contact  , name='edit_contact'),
    path('sum-form/', sum_form, name='sum_form'),
    path('download_file/',download_file, name='download_file')
]
