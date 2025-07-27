from .models import Log


class LogMixin:
    def save_log(self, table, action, data):
        Log(table=table, action=action, data=data, user=self.request.user).save()
