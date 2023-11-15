from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

host = "127.0.0.1"
db_name = "shop"
db_username = "root"
db_password = "20000908LPFc"

engine = create_engine(f'mysql+pymysql://{db_username}:{db_password}@{host}/{db_name}',
                       echo=False,
                       future=True,
                       pool_size=5,
                       pool_recycle=1800,
                       pool_timeout=60,
                       pool_pre_ping=True)

session_factory = sessionmaker(bind=engine)
db_session = scoped_session(session_factory)

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(1000), nullable=True)
    password = Column(String(1000), nullable=True)
    name = Column(String(1000), nullable=True)
    balance = Column(String(1000), nullable=True, default='5000')
    address = Column(String(1000), nullable=True)
    email = Column(String(1000), nullable=True)
    user_class = Column(String(1000), nullable=True)


class Business(Base):
    __tablename__ = 'business'
    id = Column(Integer, primary_key=True)
    username = Column(String(1000), nullable=True)
    password = Column(String(1000), nullable=True)
    name = Column(String(1000), nullable=True)
    email = Column(String(1000), nullable=True)
    business_class = Column(String(1000), nullable=True)
    wages = Column(String(1000), nullable=True)
    address = Column(String(1000), nullable=True)
    shop_name = Column(String(1000), nullable=True)


class ShopInfo(Base):
    __tablename__ = 'shop_info'
    id = Column(Integer, primary_key=True)
    business_shop_name = Column(String(1000), nullable=True)
    shop_name = Column(String(1000), nullable=True)
    shop_number = Column(String(1000), nullable=True)
    shop_price = Column(String(1000), nullable=True)


class UserBuyShopInfo(Base):
    __tablename__ = 'user_buy_shop_info'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(1000), nullable=True)
    shop_name = Column(String(1000), nullable=True)
    shop_price = Column(String(1000), nullable=True)
    shop_number = Column(String(1000), nullable=True)
    shop_total_price = Column(String(1000), nullable=True)
    shop_time = Column(String(1000), nullable=True)


class Admin(Base):
    __tablename__ = 'admin'
    id = Column(Integer, primary_key=True)
    username = Column(String(1000), nullable=True)
    password = Column(String(1000), nullable=True)


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
