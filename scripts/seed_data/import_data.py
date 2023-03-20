import os
import json
import django


def run():
    print('加载数据…')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    django.setup()
    from apps.website.models import Category, WebSite

    with open('seed_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    bulk_website = []
    for category in data:
        c_item, _ = Category.objects.get_or_create(name=category['name'])
        for website in category['sites']:
            site_item = WebSite(
                name=website['title'],
                category=c_item,
                url=website['url']
            )
            bulk_website.append(site_item)

    print('批量添加中')
    WebSite.objects.bulk_create(bulk_website)
    print(f'搞定，添加了 {len(bulk_website)} 个网站')


if __name__ == '__main__':
    run()
