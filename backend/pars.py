import json

from models import Office, Atm
from database import SessionLocal
from database import Base, engine


def delete_all():
    Base.metadata.drop_all(bind=engine)

def rename(value):
    if value == 'AVAILABLE':
        return True
    return False

def pars_atms():
    with open("data/atms.json", "r", encoding='utf-8') as file:
        data = json.load(file)
        for atm in data['atms']:
            address = atm['address']
            latitude = atm['latitude']
            longitude = atm['longitude']
            is_all_day = atm['allDay']
            services = atm['services']

            wheelchair = rename(services['wheelchair']['serviceActivity'])
            blind = rename(services['blind']['serviceActivity'])
            nfc_for_bank_cards = rename(services['nfcForBankCards']['serviceActivity'])
            qr_read = rename(services['qrRead']['serviceActivity'])
            supports_usd = rename(services['supportsUsd']['serviceActivity'])
            supports_charge_rub = rename(services['supportsChargeRub']['serviceActivity'])
            supports_eur = rename(services['supportsEur']['serviceActivity'])
            supports_rub = rename(services['supportsRub']['serviceActivity'])

            with SessionLocal() as session:
                atm_db = Atm(address=address, longitude=longitude, latitude=latitude, is_all_day=is_all_day,
                             wheelchair=wheelchair, blind=blind,
                             nfc_for_bank_cards=nfc_for_bank_cards, qr_read=qr_read, supports_rub=supports_rub,
                             supports_usd=supports_usd, supports_charge_rub=supports_charge_rub,
                             supports_eur=supports_eur)
                session.add(atm_db)
                session.commit()


def pars_offices():
    with open("data/offices2.json", "r", encoding='utf-8') as file:
        data = json.load(file)
        for office in data:
            name = office['salePointName']
            address = office['address']
            status = office['status']
            open_hours = office['openHours']
            if office['rko'] == 'есть РКО':
                rko = True
            else:
                rko = False
            open_hours_individual = office['openHoursIndividual']
            office_type = office['officeType']
            sale_point_format = office['salePointFormat']
            if office['suoAvailability'] == 'Y':
                availability = True
            else:
                availability = False
            if office['hasRamp'] == 'N':
                has_ramp = False
            else:
                has_ramp = True

            latitude = office['latitude']
            longitude = office['longitude']
            metro_station = office['metroStation']
            distance = office['distance']
            kep = office['kep']
            my_branch = office['myBranch']
            with SessionLocal() as session:

                office_db = Office(name=name, address=address, status=status, open_hours=open_hours,
                                   open_hours_individual=open_hours_individual, rko=rko, office_type=office_type,
                                   sale_point_format=sale_point_format, availability=availability, has_ramp=has_ramp,
                                   latitude=latitude, longitude=longitude, metro_station=metro_station,
                                   distance=distance,
                                   kep=kep, my_branch=my_branch
                                   )
                session.add(office_db)
                session.commit()
                session.refresh(office_db)


def redach_office():
    with SessionLocal() as session:
        db = session.query(Office).all()
        for req in db:
            mass = []
            for slovar in req.open_hours:
                dictionary = {'day': 'пн', 'hours': str(slovar['hours'])}
                mass.append(dictionary)

        req.open_hours = str(mass)

        session.add(req)
        session.commit()


def test():
    with SessionLocal() as session:
        db = session.query(Office).filter(Office.id == 1)[0]
        print(db.open_hours)



