'''Database session and engine configuration.'''

import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

logger = logging.getLogger(__name__)

MYSQL_USER = os.getenv('MYSQL_USER', 'user_placeholder')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'password_placeholder')
MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
MYSQL_DB = os.getenv('MYSQL_DB', 'folder_coding')

DATABASE_URL = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}'

engine = create_engine(DATABASE_URL, echo=False, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Session:
    '''Provide a transactional database session.'''
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.exception('Database session error: %s', e)
        raise
    finally:
        db.close()