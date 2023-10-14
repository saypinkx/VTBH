from sqlalchemy.orm import Session
from models import User, Atm
from schemas import UserCreate, AtmFilter
from sqlalchemy import and_


def get_user(db: Session, username: str) -> User:
    return db.query(User).filter(User.username == username).first()


def create_user(db: Session, user: UserCreate) -> User:
    db_user = User(email=user.email, password=user.password, username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def filter_atm(atm_filter: AtmFilter, db: Session, atms: Session = None):
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

    # atms = db.query(Atm).all()
    # filters = atm_filter.dict()
    # filters_current = []
    # result = []
    # for key in filters:
    #     if filters[key]:
    #         filters_current.append(key)
    # for atm in atms:
    #     filters_dict = {'blind': atm.blind,
    #                     'is_all_day': atm.is_all_day,
    #                     'wheelchair': atm.wheelchair,
    #                     'nfc_for_bank_cards': Atm.nfc_for_bank_cards,
    #                     'qr_read': atm.qr_read                   }
    #     flag = True
    #     for filter in filters_current:
    #         if not filters_dict[filter]:
    #             flag = False
    #     if flag:
    #         result.append(atm)
    # return result
    #

    # is_all_day = mapped_column(Boolean)
    # wheelchair = mapped_column(Boolean)
    # blind = mapped_column(Boolean)
    # nfc_for_bank_cards = mapped_column(Boolean)
    # qr_read = mapped_column(Boolean)
    # supports_usd = mapped_column(Boolean)
    # supports_charge_rub = mapped_column(Boolean)
    # supports_eur = mapped_column(Boolean)
    # supports_rub = mapped_column(Boolean)
    #
