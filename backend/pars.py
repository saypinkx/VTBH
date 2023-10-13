import json

from models import Office
from database import SessionLocal
from database import Base, engine

def delete_all():
    Base.metadata.drop_all(bind=engine)

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

# def save(db: Session, **kwargs):
#     office_db = Office(**kwargs)
#     db.add(office_db)
#     db.commit()
#     db.refresh(office_db)
#
#
# def create(db: Session = Depends(get_db), **kwargs):
#     save(db, **kwargs)
