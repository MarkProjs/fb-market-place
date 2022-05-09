import re

from django import template

register = template.Library()


@register.simple_tag
def my_url(value, field_name, urlencode=None):
    # print(value)
    # print(field_name)
    # print(urlencode)
    url = '?{}={}'.format(field_name, value)

    if urlencode:
        querystring = urlencode.split('&')
        filtered_querystring = filter(lambda p: p.split('=')[0] != field_name, querystring)
        # print(filtered_querystring)
        encoded_querystring = '&'.join(filtered_querystring)
        # print(encoded_querystring)
        url = '{}&{}'.format(url, encoded_querystring)
        # print(url)
        print('in if')
        return url
    else:
        if not field_name == 'ordering':
            url = '?{}={}'.format(field_name, value)
        print(url)
        url = '{}&{}'.format(url, 'ordering=')
        # print('in else')
        # print(url)
        # return '{}&{}'.format(url, 'ordering=')
        return url
