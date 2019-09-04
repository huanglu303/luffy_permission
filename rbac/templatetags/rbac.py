from django.template import Library
from django.conf import settings
register = Library()


@register.inclusion_tag('rbac/static_menu.html')
def static_menu(request):
    '''
    创建一级菜单
    :return:
    '''
    menu_list = request.session[settings.MENU_SISSION_KEY]
    return {"menu_list":menu_list}