import datetime
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType

from .models import Actions


def create_actions(user, verb, target):
    now = timezone.now()
    last_minute = datetime.timedelta(seconds=60)
    similar_actions = Actions.object.filter(user_id=user.id,
                                            verb=verb,
                                            created__gte=last_minute)

    if target:
        target_ct = ContentType.objects.get_for_model(target)
        similar_actions = similar_actions.objects.filter(target_ct=target_ct,
                                                         target_id=target.id)

    if not similar_actions:
        action = Actions(user=user, verb=verb, target=target)
        action.save()

        return True
    return False
