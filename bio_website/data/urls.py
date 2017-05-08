from django.conf.urls import patterns, url

from data import views

urlpatterns = patterns('',
    url(r'^$', views.mainpage, name='mainpage'),
	url(r'^database/',views.database,name='database'),
	url(r'^login/',views.login,name='login'),
	url(r'^user/',views.user,name='user'),
	url(r'^loginmid/',views.loginmid,name='loginmid'),
	url(r'^change-password/',views.change_password,name='change-password'),
	url(r'^logout/',views.logout,name='logout'),
	url(r'^usermanage/',views.usermanage,name='usermanage'),
	url(r'^fail/',views.fail,name='fail'),
	url(r'^change_password_mid/',views.change_password_mid,name='change_password_mid'),
	url(r'^addmid/',views.addmid,name='addmid'),
	url(r'^getdata/',views.getdata,name='getdata'),
	url(r'^delete/(?P<username>.+)',views.user_delete,name='user_delete'),
	url(r'^result/(?P<ID>.+)',views.result,name='result'),
	url(r'^input/',views.input,name='input'),
	url(r'^addtag/',views.addtag,name='addtag'),
	url(r'^success/',views.success,name='success'),
	url(r'^list/(?P<feature>.+)',views.list_all,name='list_all'),
	url(r'^ajax/',views.ajax,name='ajax'),
	url(r'^search_name/',views.search_name,name='search_name'),
	url(r'^search_feature/',views.search_feature,name='search_feature'),
	url(r'^data_delete/',views.data_delete,name='data_delete'),
	url(r'^tag_delete/',views.tag_delete,name='tag_delete'),


	
)
