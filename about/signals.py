from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db.models import F

from about.models import Member


@receiver(pre_save, sender=Member)
def ranking_update_if_conflict(sender, instance, **kwargs):
    # print(f"instance:::{instance}")
    # print(f"display_rank:::{instance.display_rank}")
    if Member.objects.filter(display_rank=instance.display_rank).exists():
        if not instance == Member.objects.get(display_rank=instance.display_rank):
            a = Member.objects.filter(display_rank__gte=instance.display_rank).update(
                display_rank=F('display_rank') + 1)


#     display_rank_updater(instance.display_rank)


# def display_rank_updater(display_rank):
#     print(f"display_rank_updater")
