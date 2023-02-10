from .models import Course


def all_object(object):
    return object.all()


def fillter(object, filter):
    print(filter)
    return object.order_by(f'-{filter}')
