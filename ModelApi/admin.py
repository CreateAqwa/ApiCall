from django.contrib import admin

# Register your models here.
from ModelApi.models import FeedbackForm,Video,Blog,Products

    # list_display=('Patientname','Mobileno','Disease')
    # list_display=('BlogDiscription','Photo','Video','BlogTitle')
    # list_display=('Video')
    
admin.site.register(FeedbackForm);
admin.site.register(Blog);
admin.site.register(Video);
admin.site.register(Products);



