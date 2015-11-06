from django.db import models

# Create your models here.


class Author(models.Model):
	AuthorID = models.AutoField(primary_key = True)
	Name = models.CharField(max_length = 20, default = "Unknow Name")
	Age = models.IntegerField(null = True, default = 18)
	Country = models.CharField(max_length = 13, default="China")
	class Meta:
		db_table = "Author"


	def __unicode__(self):
		return self.Name

class Book(models.Model):
	ISBN = models.CharField(max_length = 20, default="XXXXXXXX", primary_key = True)
	Title = models.CharField(max_length = 100, default="Unknow Book")
	Publisher = models.CharField(max_length = 20, null = True)
	PublishDate = models.DateField(null = True)
	Price = models.FloatField(null = True)
	Author = models.ForeignKey(Author)
	class Meta:
		db_table = "Book"

	def __unicode__(self):
		return self.Title