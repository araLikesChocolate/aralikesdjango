from django.db import models

# Create your models here.
# Create your models here.
class Member(models.Model) :
    idx = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    id = models.CharField(max_length=255)
    service_type = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
            db_table = u'member' 

    def __str__(self) :
        return 'idx: {}, email: {}, id: {}, type: {}'.format(self.idx, self.email, self.id, self.service_type)