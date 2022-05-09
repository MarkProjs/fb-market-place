from django import template

register = template.Library()


@register.simple_tag
def my_url(value, field_name, urlencode=None):
    # print('value='+value+', field='+field_name+', enc='+urlencode)
    print(value)
    print(field_name)
    print(urlencode)
    url = '?{}={}'.format(field_name, value)

    if urlencode:
        querystring = urlencode.split('&')
        filtered_querystring = filter(lambda p: p.split('=')[0] != field_name, querystring)
        encoded_querystring = '&'.join(filtered_querystring)
        url = '{}&{}'.format(url, encoded_querystring)

        return url
