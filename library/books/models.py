from django.db import models

# Create your models here.
class Publishers(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Authors(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Books(models.Model):

    class LCC(models.TextChoices):
        GENERAL_WORK = 'A', 'General Works'
        PHILOSOPHY_PSYCHOLOGY_RELIGION = 'B', 'Philosophy, Psychology, Religion'
        AUXILIARY_SCIENCES_OF_HISTORY = 'C', 'Auxiliary Sciences of History'
        WORLD_HISTORY_AND_HISTORY_OF_CONTINENTS = 'D', 'World History and History of Europe, Asia, Africa, Australia, New Zealand, etc'
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

    authorship = models.ForeignKey(
        Authors, 
        related_name="books", 
        verbose_name="Book's authorship", 
        help_text="Enter author's name", 
        db_index=True, 
        on_delete=models.CASCADE
        )
    
    year = models.PositiveIntegerField(
        verbose_name="Book's publication Year", 
        help_text="Enter book's year", 
        db_index=True
        )
    
    title = models.CharField(
        max_length=150, 
        verbose_name="Book's title", 
        help_text="Enter book's title"
        )
    
    publisher = models.ForeignKey(
        Publishers, 
        verbose_name="Book's publisher", 
        help_text="Enter publisher's name", 
        db_index=True, 
        on_delete=models.CASCADE
        )
    
    category = models.CharField(
        max_length=1, 
        choices=LCC.choices, 
        verbose_name="Book's LCC", 
        help_text="Enter book's LCC", 
        db_index=True
        )
    
    language = models.CharField(
        max_length=3, 
        choices=Languages.choices, 
        verbose_name="Book's language", 
        help_text="Enter book's language", 
        db_index=True
        )

    def __str__(self):
        category_display = dict(Books.LCC.choices).get(self.category, 'Unknown Category')
        language_display = dict(Books.Languages.cbhoices).get(self.language, 'Unknown Language')

        return (
            f"{self.authorship} ({self.year}). {self.title}. {self.publisher}. {category_display}. {language_display}."
        )

"""
LAST NAME, First Name (year). Title. Publisher. Category. Language.
"""