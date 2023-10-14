from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Boolean, JSON, Numeric
from sqlalchemy.orm import mapped_column
from datetime import datetime
from database import Base


class User(Base):
    __tablename__ = "User"
    id = mapped_column("id", Integer, primary_key=True, autoincrement=True)
    email = mapped_column("email", String, nullable=True)
    username = mapped_column("username", String, nullable=False)
    password = mapped_column("password", String, nullable=False)
    registered_at = mapped_column("registered_at", TIMESTAMP, default=datetime.utcnow)
    is_superuser = mapped_column("is_superuser", Boolean, default=False)
    is_entity = mapped_column("is_entity", Boolean, default=False)
    is_active = mapped_column("is_active", Boolean, default=False)


class Office(Base):
    __tablename__ = 'office'
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String)
    address = mapped_column(String)
    latitude = mapped_column(String)
    longitude = mapped_column(String)
    office_type = mapped_column(String)
    sale_point_format = mapped_column(String)
    availability = mapped_column(Boolean)
    has_ramp = mapped_column(Boolean)
    metro_station = mapped_column(String, nullable=True, default=None)
    distance = mapped_column(Integer)
    kep = mapped_column(Boolean)
    my_branch = mapped_column(Boolean)
    open_hours = mapped_column(JSON)
    open_hours_individual = mapped_column(JSON)
    rko = mapped_column(Boolean)
    status = mapped_column(String)


class Atm(Base):
    __tablename__ = 'Atm'
    id = mapped_column(Integer, autoincrement=True, primary_key=True)
    address = mapped_column(String)
    latitude = mapped_column(String)
    longitude = mapped_column(String)
    is_all_day = mapped_column(Boolean)
    wheelchair = mapped_column(Boolean)
    blind = mapped_column(Boolean)
    nfc_for_bank_cards = mapped_column(Boolean)
    qr_read = mapped_column(Boolean)
    supports_usd = mapped_column(Boolean)
    supports_charge_rub = mapped_column(Boolean)
    supports_eur = mapped_column(Boolean)
    supports_rub = mapped_column(Boolean)





