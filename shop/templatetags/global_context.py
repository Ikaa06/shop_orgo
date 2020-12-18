from shop.models import BasicInfo


def get_info(request):
    base_info = BasicInfo.objects.first()
    return {"info": base_info}