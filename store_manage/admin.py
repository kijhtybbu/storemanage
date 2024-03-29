from django.contrib import admin

# Register your models here.

from .models import StoreInformation, StoreComment


class StoreCommentInline(admin.StackedInline):
    model=StoreComment
    extra = 2


class StoreInformationAdmin(admin.ModelAdmin):
    fields = (('brand', 'code'),
              ('name', 'address'),
              'contacts',
              ('equipment_arrival_date', 'completion_date'),
              ('expected_installation_date', 'Opening_date'),
              'closed_date',
              'engineering_head',
              'ip',
              'firewall_type',
              ('ap', 'guest_wifi'),
              'status',
              'ps')
    list_display = ('code', 'name', 'ip', 'engineering_head', 'status', 'Opening_date', 'closed_date',)
    date_hierarchy = 'Opening_date'
    empty_value_display = '(None)'
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-Opening_date',)

    # list_editable 设置默认可编辑字段
    # list_editable = ['machine_room_id', 'temperature']
    list_filter = ('status', 'expected_installation_date', 'closed_date')  # 过滤器
    search_fields = ('code', 'name')  # 搜索字段
    inlines = [StoreCommentInline]

    def get_changeform_initial_data(self, request):
        return {'ip': '12.12.12.12'}


admin.site.site_header = '店铺管理'
admin.site.site_title = '店铺管理系统'
admin.site.register(StoreInformation, StoreInformationAdmin)


