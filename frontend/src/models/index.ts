export interface AtmFilter {
  is_all_day: boolean;
  wheelchair: boolean;
  blind: boolean;
  nfc_for_bank_cards: boolean;
  qr_read: boolean;
  supports_usd: boolean;
  supports_charge_rub: boolean;
  supports_eur: boolean;
  supports_rub: boolean;
}

export interface Atm extends AtmFilter {
  address: string;
  latitude: string;
  longitude: string;
}

export interface Credentials {
  username: string;
  password: string;
}

export interface LoginInfo {
  access_token: string;
  user_role: string;
}

export interface UserFile {
  date: string;
  id?: string;
  name: string;
  result?: string;
  size: number;
}

export interface UserInfo {
  email: string;
  id: number;
  username: string;
  role: string;
}
