from django.utils.crypto import get_random_string
from .models import Media

def generateUID():
    uid = get_random_string(length=16, allowed_chars=u'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    date = datetime.datetime.now()

    result = '%s-%s-%s_%s' % (date.year, date.month, date.day, uid)
    print(result)

    try:
        obj = Media.objects.get(uid=result)
    except Media.DoesNotExist:
        return uid
    else:
        return generateUID()
