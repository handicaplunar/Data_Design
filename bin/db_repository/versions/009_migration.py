from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
library = Table('library', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('body', String(length=140)),
    Column('type', String(length=140)),
    Column('author', String(length=140)),
    Column('no_of_books', Integer),
    Column('name', String(length=140)),
    Column('timestamp', DateTime),
    Column('user_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['library'].columns['author'].create()
    post_meta.tables['library'].columns['name'].create()
    post_meta.tables['library'].columns['no_of_books'].create()
    post_meta.tables['library'].columns['type'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['library'].columns['author'].drop()
    post_meta.tables['library'].columns['name'].drop()
    post_meta.tables['library'].columns['no_of_books'].drop()
    post_meta.tables['library'].columns['type'].drop()
