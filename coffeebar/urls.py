from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'coffeebar'

order = [
    url(r'^$', views.order_details, name='index'),
    url(r'^(?P<order_id>[0-9]+)/$', views.order_details, name='details'),

    url(r'^add/$', views.order_add_item, name='add'),
    url(r'^remove/$', views.order_remove_item, name='remove'),
    url(r'^checkout/$', views.order_checkout, name='checkout'),
    url(r'^list/$', views.order_list, name='list'),
]

admin = [
    url(r'^$', views.admin, name='index'),
    url(r'^accounts/', include([
        url(r'^$', views.admin_accounts, name='index'),
        url(r'^open/$', views.admin_accounts, {'action': 'open'}, name='open'),
        url(r'^close/$', views.admin_accounts, {'action': 'close'}, name='close'),
    ], namespace='accounts')),

    url(r'^orders/', include([
        url(r'^$', views.admin_orders, name='index'),
        url(r'^update/', views.admin_orders, {'action': 'update'}, name='update'),
    ], namespace='orders')),

    url(r'^products/', include([
        url(r'^$', views.admin_products, name='index'),
        url(r'^add/$', views.admin_products, {'action': 'add'}, name='add'),
        url(r'^(?P<product_id>[0-9]+)/', views.admin_products, {'action': 'edit'}, name='edit'),
        url(r'^(?P<product_id>[0-9]+)/toggle/$', views.admin_products, {'action': 'toggle'}, name='toggle'),
        url(r'^(?P<product_id>[0-9]+)/delete/$', views.admin_products, {'action': 'delete'}, name='delete'),
    ], namespace='products')),
]

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'order/', include(order, namespace='order')),
    url(r'admin/', include(admin, namespace='admin')),

    # django auth
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logout.html'}, name='logout'),
]
