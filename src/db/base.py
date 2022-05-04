import re

from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import as_declarative, declared_attr

# Default naming convention for all indexes and constraints
# See why this is important and how it would save your time:
# https://alembic.sqlalchemy.org/en/latest/naming.html
convention = {
    'all_column_names': lambda constraint, table: '_'.join([
        column.name for column in constraint.columns.values()
    ]),
    'ix': 'ix__%(table_name)s__%(all_column_names)s',
    'uq': 'uq__%(table_name)s__%(all_column_names)s',
    'ck': 'ck__%(table_name)s__%(constraint_name)s',
    'fk': (
        'fk__%(table_name)s__%(all_column_names)s__'
        '%(referred_table_name)s'
    ),
    'pk': 'pk__%(table_name)s'
}

# Registry for all tables
metadata = MetaData(naming_convention=convention)


@as_declarative(metadata=metadata)
class Base(object):
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls):
        words = re.split('(?<=[^A-Z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])', cls.__name__)

        return '_'.join(words).lower()
