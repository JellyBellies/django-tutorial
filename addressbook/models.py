from django.db import models

class Title(models.Model):
    # example table for titles available
    title_name = models.CharField(max_length=5)
    def __unicode__(self):
        return self.title_name

class City(models.Model):
    # example table of cities, populated with only a few examples
    # table can be populated using source files listing all cities
    city_name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.city_name

class County(models.Model):
    # example table of counties, populated with only a few examples
    # as above, table can be populated using source files listing all counties
    county_name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.county_name

class Record(models.Model):
    # stores all attributes provided
    # some attributes, such as title, city and county can be selected by drop down
    # such predictable attributes are best stored in a seperate table
    # enables more fluid population of drop down menus and improved normalisation
    title = models.ForeignKey(Title)
    firstname = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    address_line_1 = models.CharField(max_length=30)
    address_line_2 = models.CharField(max_length=30, blank=True, null=True)
    address_line_3 = models.CharField(max_length=30, blank=True, null=True)
    city = models.ForeignKey(City)
    county = models.ForeignKey(County)
    postcode = models.CharField(max_length=8)
    def __unicode__(self):
        st = self.title.title_name + " " + self.firstname + " " + self.surname
        return st
    def get_name(self):
        st = self.title.title_name + " " + self.firstname + " " + self.surname
        return st
    def get_address(self):
        st = self.address_line_1 + ",\n" + self.address_line_2 + ",\n" + self.address_line_3
        return st
    get_address.short_description = 'Address'
    get_name.short_description = 'Name'
