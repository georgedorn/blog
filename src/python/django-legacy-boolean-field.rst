Legacy BooleanField in Django
#############################

:date: 2010/11/29
:tags: django, python

A legacy BooleanField supporting all kinds of antiquated ways of storing boolean values.
========================================================================================

Django's inspectdb is pretty good at providing models that will at least read and write from your legacy database.  But to get real power out of the ORM, you may need to provide some custom mapping for fields that don't behave exactly the way Django expects them to. 

It's not terribly hard to subclass Django models and provide additional functionality.  One thing that's missing from the BooleanField, for example, is support for legacy dbs that use really lame storage mechanisms like Y/N or 1/0, or even better, enum('True','False).  The enum case is extra hilarious when you discover that mysql stores that as "True" = 0 and "False" = 1.

Here's a highly flexible legacy field:

.. code-block:: python

 from django.db import models


 class LegacyBooleanField(models.BooleanField):
     __metaclass__ = models.SubfieldBase #need this for django to know to call to_python()

     def __init__(self, for_true='Y', for_false='N', db_type='char(1)', *args, **kwargs):
         super(LegacyBooleanField, self).__init__(*args, **kwargs)
         self.for_true = for_true
         self.for_false = for_false
         self._db_type = db_type

     def db_type(self, connection):
         return self._db_type

     def to_python(self, value):
         if value in (True, False):
             return bool(value)
         if value == self.for_true:
             return True
         if value == self.for_false:
             return False
         raise models.ImproperlyConfigured("LegacyBooleanField %s contained invalid element %s, not one of (%s, %s)" % (self.db_column, value, self.for_true, self.for_false))

     def get_prep_value(self, value):
         if value in (self.for_true, self.for_false):
             return value
         if value is True:
             return self.for_true
         if value is False:
             return self.for_false

     def get_prep_lookup(self, lookup_type, value):
         if value in ('1','0'): #special case for dealing with admin, see BooleanField.get_prep_lookup
             value = bool(value)
         if lookup_type == 'exact':
             return self.get_prep_value(value)
         else:
             raise TypeError('Lookup type %r not supported.' % lookup_type)



And now to use it, here's several examples:


.. code-block:: python

 from django.db import models
 from legacy.fields import LegacyBooleanField

 class MyModel(models.Model):
     yn_field = LegacyBooleanField(for_true='Y', for_false='N', db_column='is_yn')
     one_zero_field = LegacyBooleanField(for_true=1, for_false=0, db_type='tinyint', db_column='is_one_zero')
     enum_field = LegacyBooleanField(for_true='True', for_false='False', db_type='char(5)', db_column='my_lame_enum_field')

This allows you to use it like a proper python boolean, including in querysets:

.. code-block:: python

 obj = MyModel.objects.get(id=1234)
 print obj.yn_field  #prints True or False
 obj.yn_field = False 
 obj.save() #converts to 'N' behind the scenes
 obj.yn_field = 'N'  #raises an error

 objs = MyModels.objects.filter(enum_field=True).filter(one_zero_field=False)



(Update 12-15-2010: Forgot __metaclass__, which is `vital <https://docs.djangoproject.com/en/dev/howto/custom-model-fields/#the-subfieldbase-metaclass>`_.)
