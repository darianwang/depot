
from django.conf.urls.defaults import *
from models import *
from views import *

urlpatterns = patterns('',

    (r'product/create/$', create_product),
    (r'product/list/$', list_product ),
    (r'product/edit/(?P<id>[^/]+)/$', edit_product),
    (r'product/view/(?P<id>[^/]+)/$', view_product),
    
)
