from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def index(request):
    """博客主页"""
    context = {
        'href_list': [
            {'href': 'https://www.baidu.com', 'name': '百度'},
            {'href': 'http://www.4399.com', 'name': '4399'},
            {'href': 'http://d.chinacycc.com/index.php?m=Login&a=index', 'name': '子域名爆破'},
            {'href': 'https://www.reg007.com/', 'name': 'REG007'},
            {'href': 'http://www.arkiller.com', 'name': 'arkiller'},
            {'href': 'http://127.0.0.1/blog/note/?nid=1', 'name': 'web安全学习笔记'},
        ]

    }
    return render(request, 'blog/index.html', context=context)


def webSecurity(request):
    nid = request.GET.get('nid')
    return render(request, f'blog/note/{nid}.html')
