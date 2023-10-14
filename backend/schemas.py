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
    is_all_day: bool
    wheelchair: bool
    blind: bool
    nfc_for_bank_cards: bool
    qr_read: bool
    supports_usd: bool
    supports_charge_rub: bool
    supports_eur: bool
    supports_rub: bool

    class Config:
        orm_mode = True
