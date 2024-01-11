from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

POSTGRES_DATABASE_URL = "postgresql://JalilUmar:VFf7lWPBU5oK@ep-noisy-hall-67483896.us-east-2.aws.neon.tech/neondb?sslmode=require"

engine = create_engine(POSTGRES_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
