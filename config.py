import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self) -> None:
        # Direct values set kiye gaye
        self.API_ID: str = "25945995"
        self.API_HASH: str = "8bc07ca966ad72c1a51a1529cf99a3ca"
        self.SESSION: str = "BQGL54sAR5pKJQveQdrbRYAGBQhBOix5SAMn4pM5DeWbRUXR8mbVZDs58BQD5qO-NTYReABY9Y7Xu1KyBZKsbj8ZwbQzxSpnSHNsi1KNhs5knz_SAv0jl1Rp2lTZKMMymn679b3m038TgWWP6H3jNUkHfZA6thCeIlPwrHB4iFf_HpwgefuM7XjVyJc7k-cDNvfbJq6waU_3o1UYQLakPXvqUuDmhL9oy5HrvUYN5_qkujYguZD5_BEuBRs6DisQeiy2RGy5r9x_k9d7Hlupgj5Ofy6iTy6z27dYHT4iRdD_1E17P5iqJ13RQiJy2Jn1Y1z5vug-azToivJDTzONS9yLXmeu9QAAAAHyBXr2AQ"
        self.BOT_TOKEN: str = "8142303286:AAEMTPoKRaMa0TkwjgIHd0Q9Vkevc0Na0nc"

        # Optional configs
        self.SUDOERS: list = [123456789]  # yaha apna Telegram ID dal sakte ho (sudo user)
        self.SPOTIFY: bool = False
        self.QUALITY: str = "high"
        self.PREFIXES: list = ["!"]   # Commands ke liye prefix (!play, !stop)
        self.LANGUAGE: str = "en"
        self.STREAM_MODE: str = "audio"
        self.ADMINS_ONLY: bool = False
        self.SPOTIFY_CLIENT_ID: str = None
        self.SPOTIFY_CLIENT_SECRET: str = None

config = Config()
