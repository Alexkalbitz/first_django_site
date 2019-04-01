from django.db import models

#class Test(models.Model):
    #dateadded = models.DateTimeField()
    #url = models.TextField()
    #headline = models.TextField()
    #source = models.TextField()

    #def __str__(self):
        #return "%s %s" % (self.source, self.headline)

class Newsdatabase(models.Model):
    dateadded = models.DateTimeField()
    url = models.TextField()
    headline = models.TextField()
    source = models.TextField()

    def __str__(self):
        return "%s %s" % (self.source, self.headline)



'''class Newsdb(models.Model):
    news_id = models.AutoField(primary_key=True)
    dateadded = models.DateTimeField()
    url = models.TextField()
    headline = models.TextField()
    source = models.TextField()

    def __str__(self):
        return "%s %s" % (self.source, self.headline)'''
