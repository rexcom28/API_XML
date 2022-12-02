from django.contrib.contenttypes.models import ContentType


def app_labels(request):
    app_labels = ContentType.objects.exclude(app_label__in=['sessions','auth','authtoken','admin','contenttypes', 'contactforms']).values('app_label').distinct()
    
    return {'app_labels':app_labels}