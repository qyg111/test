from django.conf.urls import url
from order.views import OrderPlaceView, OrderCommitView,CommentView

urlpatterns = [
    url(r'^place$', OrderPlaceView.as_view(), name='place'), # 提交订单页面显示
    url(r'^commit$', OrderCommitView.as_view(), name='commit'), # 订单创建
    url(r'^comment/(?P<order_id>.+)$', CommentView.as_view(), name='comment'),  # 订单评论
]
