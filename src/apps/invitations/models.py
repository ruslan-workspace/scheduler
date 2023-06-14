from django.db import models


class InvitationStatus(models.IntegerChoices):
    PENDING = 1, "Pending"  # ожидание ответа
    ACCEPTED = 2, "Accepted"  # принято
    DECLINED = 3, "Declined"  # отклонено
    CANCELED = 4, "Canceled"  # отменено


class Invitation(models.Model):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="scheduled_users"
    )
    event = models.ForeignKey(
        "events.Event", on_delete=models.CASCADE, related_name="invaitations"
    )
    status = models.PositiveSmallIntegerField(
        choices=InvitationStatus.choices, default=InvitationStatus.PENDING
    )
