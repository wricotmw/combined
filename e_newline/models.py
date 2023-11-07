from django.db import models


# Create your models here.
class Dances(models.Model):
	select_level = (
        ('beg', 'beg'),
        ('imp', 'imp'),
        ('int', 'int'),
        )

	name = models.CharField('name', max_length=120)
	video_id = models.CharField('video_id', blank=True, max_length=50)
	level = models.CharField('level', max_length=3,choices=select_level)
	steps = models.URLField('steps', max_length=150, blank=True)
	
	def __str__(self):
		return str(self.name)
