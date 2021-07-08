import databases
import sqlalchemy

from .conf import settings





URL_DATA_BASE = (
                'postgresql://'
                f'{settings.postgres_user}:'
                f'{settings.postgres_password}'
                '@dat:5432/'
                f'{settings.postgres_db}'
                )
# URL_DATA_BASE = "postgresql://postgres:postgres@localhost/t5"

database = databases.Database(URL_DATA_BASE)
engine = sqlalchemy.create_engine(URL_DATA_BASE)
metadata = sqlalchemy.MetaData()