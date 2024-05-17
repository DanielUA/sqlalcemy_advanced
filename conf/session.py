from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# an Engine, which the Session will use for connection
# resources, typically in module scope
POSTGRES_URL = "postgresql+psycopg2://postgres:example@localhost:5432/postgres"
engine = create_engine(POSTGRES_URL, echo=True, pool_size=5, max_overflow=0)

# a sessionmaker(), also in the same scope as the engine
Session = sessionmaker(engine)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
