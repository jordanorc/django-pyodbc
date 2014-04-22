import copy
import datetime

from django.utils import six
from django.db.backends.schema import BaseDatabaseSchemaEditor
from django.db.utils import DatabaseError


class DatabaseSchemaEditor(BaseDatabaseSchemaEditor):

    sql_create_column = "ALTER TABLE %(table)s ADD %(column)s %(definition)s"
    sql_alter_column_type = "ALTER COLUMN %(column)s %(type)s"
    sql_alter_column_null = "ALTER COLUMN %(column)s %(type)s NULL"
    sql_alter_column_not_null = "ALTER COLUMN %(column)s %(type)s NOT NULL"
    #TODO??
    sql_alter_column_default = "ALTER COLUMN %(column)s DEFAULT %(default)s"
    sql_alter_column_no_default = "ALTER COLUMN %(column)s DEFAULT NULL"
    
    sql_delete_column = "ALTER TABLE %(table)s DROP COLUMN %(column)s"
    sql_delete_table = "DROP TABLE %(table)s CASCADE CONSTRAINTS"

    def __enter__(self):
        self.deferred_sql = []
        return self