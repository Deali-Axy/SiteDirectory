def get_ip(request):
    """
    获取IP地址
    参考：https://pythonguides.com/get-user-ip-address-in-django/

    :param request:
    :return:
    """
    user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip:
        ip = user_ip.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip
