from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql+psycopg2://training_6fkj_user:u7ggyCXcP1HhmCmsxaoXfcELKIphQvT0@dpg-dbbfh5e7bikc738d0h50-a.oregon-postgres.render.com/training_6fkj"

# DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/training"
engine = create_engine(DATABASE_URL)
localSession = sessionmaker(autocommit = False,autoflush = False,bind=engine)
base = declarative_base () 
def get_db():
    db = localSession()
    try:
        yield db 

    finally:
        db.close()
