from sqlalchemy.orm import Session
from models import User, Atm, Office
from schemas import UserCreate, AtmFilter, OfficeFilter
from sqlalchemy import and_


def get_user(db: Session, username: str) -> User:
    return db.query(User).filter(User.username == username).first()


def create_user(db: Session, user: UserCreate) -> User:
    db_user = User(email=user.email, password=user.password, username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def filter_atm(atm_filter: AtmFilter, db: Session):
    filters_dict = {'blind': Atm.blind,
                    'is_all_day': Atm.is_all_day,
                    'wheelchair': Atm.wheelchair,
                    'nfc_for_bank_cards': Atm.nfc_for_bank_cards,
                    'qr_read': Atm.qr_read,
                    'supports_usd': Atm.supports_usd,
                    'supports_eur': Atm.supports_eur,
                    'supports_rub': Atm.supports_rub,
                    'supports_charge_rub': Atm.supports_charge_rub,
                    }
    current_filters = atm_filter.dict()
    atms = db.query(Atm)
    for key in current_filters:
        if current_filters[key]:
            atms = atms.filter(filters_dict[key] == 1)
    return atms.all()


def filter_office(office_filter: OfficeFilter, db: Session):
    filters_dict = {'has_ramp': Office.has_ramp,
                    'kep': Office.kep,
                    'my_branch': Office.my_branch,
                    'rko': Office.rko,
                    'status': Office.status
                    }
    current_filters = office_filter.dict()
    offices = db.query(Office)
    for key in current_filters:
        if current_filters[key]:
            offices = offices.filter(filters_dict[key] == 1)

    return offices.all()
