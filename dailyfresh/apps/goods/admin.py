from django.contrib import admin
from django.core.cache import cache
from goods.models import GoodsType,IndexPromotionBanner,IndexTypeGoodsBanner,IndexGoodsBanner,GoodsSKU,Goods


class BaseModelAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        '''新增或者更新表中的数据时调用'''
        super().save_model(request,obj,form,change)

        # 发出任务，让celery worker重新生成首页静态页
        from celery_tasks.tasks import generate_static_index_html
        generate_static_index_html.delay()

        # 删除缓存
        cache.delete('index_page_data')
    def delete_model(self, request, obj):
        '''删除表中的数据时调用'''
        super().delete_model(request,obj)
        from celery_tasks.tasks import generate_static_index_html
        generate_static_index_html.delay()

        cache.delete('index_page_data')

class IndexPromotionBannerAdmin(BaseModelAdmin):
    pass

class GoodsTypeAdmin(BaseModelAdmin):
    pass

class IndexTypeGoodsBannerAdmin(BaseModelAdmin):
    pass

class IndexGoodsBannerAdmin(BaseModelAdmin):
    pass
class GoodsSKUAdmin(BaseModelAdmin):
    pass
class GoodsAdmin(BaseModelAdmin):
    pass

# Register your models here.
admin.site.register(GoodsType,GoodsTypeAdmin)
admin.site.register(IndexGoodsBanner,IndexGoodsBannerAdmin)
admin.site.register(IndexTypeGoodsBanner,IndexTypeGoodsBannerAdmin)
admin.site.register(IndexPromotionBanner, IndexPromotionBannerAdmin)
admin.site.register(GoodsSKU, GoodsSKUAdmin)
admin.site.register(Goods, GoodsAdmin)