from django import template

register = template.Library()

from tools.jalali import *
from tools.formatter import *
from back.models import Profile


# {% current_time "%d/%m/%Y %H:%M:%S %p" %}
@register.simple_tag
def current_time(format_string):
    return datetime.now().strftime(format_string)


def type_splitter(type):
    return type.split('__')[0]


# {% current_date_persian %}
@register.simple_tag
def current_date_persian():
    a = datetime_to_jalali(datetime.now())
    return eng_to_persian_number("{}/{}/{}".format(a[2], a[1], a[0]))


# Filter => {{week_day|weekd:"fa"}} or {{week_day|weekd:"en"}}
def weekd(week_day, lang):
    if lang == "fa":
        return week_map(week_day)
    if lang == "en":
        return persian_to_eng_number(week_day)
    else:
        return week_day


# Filter => {{num|l10n_num:"fa"}} or {{num|l10n_num:"en"}}
def l10n_num(num, lang):
    if lang == "fa":
        return eng_to_persian_number(num)
    if lang == "en":
        return persian_to_eng_number(num)
    else:
        return num


def modify_week(value, arg):
    # if arg is first_name: return the first string before space
    if arg == "first_name":
        return value.split(" ")[0]
    # if arg is last_name: return the last string before space
    if arg == "last_name":
        return value.split(" ")[-1]
    # if arg is title_case: return the title case of the string
    if arg == "title_case":
        return value.title()
    return value


def get_pr_name(username):
    try:
        pr = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
        return 'unknown'
    return "{} {}".format(pr.name, pr.last_name)


def key_name(dic, key):
    try:
        return dic[key]['pr_name']
    except:
        pass


def key_phone(dic, key):
    try:
        return dic[key]['phone']
    except:
        pass


register.filter('key_name', key_name)
register.filter('key_phone', key_phone)
register.filter('type_splitter', type_splitter)
register.filter('modify_week', modify_week)
register.filter('l10n_num', l10n_num)
register.filter('weekd', weekd)
register.filter('get_pr_name', get_pr_name)
