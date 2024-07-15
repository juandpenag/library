from django.db import models

# Create your models here.

class LCC(models.TextChoices):
    GENERAL_WORK = 'A', 'General Works'
    PHILOSOPHY_PSYCHOLOGY_RELIGION = 'B', 'Philosophy, Psychology, Religion'
    AUXILIARY_SCIENCES_OF_HISTORY = 'C', 'Auxiliary Sciences of History'
    WORLD_HISTORY_AND_HISTORY_OF_CONTINENTS = 'D', 'World History and History of Europe, Asia, Africa, Australia, New Zealand, etc.'
    HISTORY_OF_AMERICA = 'E', 'History of America'
    HISTORY_OF_THE_AMERICAS = 'F', 'History of the Americas'
    GEOGRAPHY_ANTHROPOLOGY_AND_RECREATION = 'G', 'Geography, Anthropology, and Recreation'
    SOCIAL_SCIENCES = 'H', 'Social Sciences'
    POLITICAL_SCIENCE = 'J', 'Political Science'
    LAW = 'K', 'Law'
    EDUCATION = 'L', 'Education'
    MUSIC = 'M', 'Music'
    FINE_ARTS = 'N', 'Fine Arts'
    LANGUAGE_AND_LITERATURE = 'P', 'Language and Literature'
    SCIENCE = 'Q', 'Science'
    MEDICINE = 'R', 'Medicine'
    AGRICULTURE = 'S', 'Agriculture'
    TECHNOLOGY = 'T', 'Technology'
    MILITARY_SCIENCE = 'U', 'Military Science'
    NAVAL_SCIENCE = 'V', 'Naval Science'
    GENERAL_INFORMATION_RESOURCES = 'Z', 'Bibliography, Library Science, and General Information Resources'

class Languages(models.TextChoices):
    SPANISH = 'SPA', 'Spanish'
    ENGLISH = 'ENG', 'English'
    FRENCH = 'FRE', 'French'

class Publishers(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Authors(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Books(models.Model):
    authorship = models.ManyToManyField(Authors, related_name="books")
    year = models.PositiveIntegerField(max_length=4)
    title = models.CharField(max_length=150)
    publisher = models.ForeignKey(Publishers)
    category = models.CharField(max_length=1, choices=LCC.choices)
    language = models.CharField(max_length=1, choices=Languages)

    def __str__(self):
        return f"{self.authorship} ({self.year}). {self.title}. {self.publisher}. {self.category}."

"""
LAST NAME, First Name (year). Title. Publisher. Category. Language.
"""