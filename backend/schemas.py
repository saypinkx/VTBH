from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    username: str
    password: str

    class Config:
        orm_mode = True


class AtmFilter(BaseModel):
    is_all_day: bool = False
    wheelchair: bool = False
    blind: bool = False
    nfc_for_bank_cards: bool = False
    qr_read: bool = False
    supports_usd: bool = False
    supports_charge_rub: bool = False
    supports_eur: bool = False
    supports_rub: bool = False

    class Config:
        orm_mode = True


class AtmResponse(BaseModel):
    address: str
    latitude: str
    longitude: str
    is_all_day: bool | None
    wheelchair: bool | None
    blind: bool | None
    nfc_for_bank_cards: bool | None
    qr_read: bool | None | None
    supports_usd: bool | None
    supports_charge_rub: bool | None
    supports_eur: bool | None
    supports_rub: bool | None

    class Config:
        orm_mode = True

class OfficeFilter(BaseModel):
    #office_type: str
    #availability: bool
    has_ramp:  bool = False
    #distance: int
    kep: bool = False
    my_branch: bool = False
    # is_individual: bool
    rko: bool = False
    status: bool = False

    class Config:
        orm_mode = True

class OfficeResponse(BaseModel):
    name: str
    address: str
    latitude: str
    longitude: str
    office_type: str
    sale_point_format: str
    availability: bool | None
    has_ramp: bool | None
    metro_station: str | None
    distance: int
    kep: bool | None
    my_branch: bool | None
    open_hours: list[dict]
    open_hours_individual: list[dict]
    rko: bool | None
    status: bool | None

