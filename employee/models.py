from django.db import models

class Employee(models.Model):
    eid=models.CharField(max_length=20)
    ename=models.CharField(max_length=100)
    eemail=models.EmailField()
    econtact=models.CharField(max_length=11)

    def _str_(self):
        return "%s" %(self.ename)
    
    class Meta:
        db_table="emplyee"