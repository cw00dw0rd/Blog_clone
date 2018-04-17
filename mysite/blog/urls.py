from django.conf.urls import url
from django.contrib.admin.views.decorators import staff_member_required
from blog import views

urlpatterns = [
    url(r'^$',views.PostListView.as_view(),name='post_list'),
    url(r'^about/$',views.AboutView.as_view(),name='about'),
    url(r'^post_list/$',views.PostListView.as_view(),name='post_list'),
    url(r'^post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name='post_detail'),
    url(r'^post/new/$',staff_member_required(views.CreatePostView.as_view()),name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$',staff_member_required(views.PostUpdateView.as_view()),name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$',staff_member_required(views.PostDeleteView.as_view()),name='post_remove'),
    url(r'^drafts/$',staff_member_required(views.DraftlistView.as_view()),name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/comment/$',views.add_comment_to_post,name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$',staff_member_required(views.comment_approve),name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$',staff_member_required(views.comment_remove),name='comment_remove'),
    url(r'^post/(?P<pk>\d+)/publish/$',staff_member_required(views.post_publish),name='post_publish'),
    url(r'^signup/$',views.signup.as_view(), name='signup'),


]
