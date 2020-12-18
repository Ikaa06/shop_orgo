from django.templatetags.tz import register
import pymorphy2


@register.filter
def look_title(number):
    morph = pymorphy2.MorphAnalyzer()
    butyavka = morph.parse('студент')[0]
    return f'{number} {butyavka.make_agree_with_number(number).word}'


@register.filter
def look_lesson(number):
    morph = pymorphy2.MorphAnalyzer()
    butyavka = morph.parse('урок')[0]
    return f'{number} {butyavka.make_agree_with_number(number).word}'
