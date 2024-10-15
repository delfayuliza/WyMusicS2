import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("7841390996:AAGbfknREI4uqgPd_UkTAv4Z5xZPR_ph_x0")
BOT_NAME = getenv("BOT_NAME", "Miwaa 𝕩 Music")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/20147c4f049e2c1f2f248.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/6809135960af808e931b9.png")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/7ffd2c88f5275fc9058eb.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/1e01db4b4bde83842e8d7.png")
admins = {}
API_ID = int(getenv("25375117"))
API_HASH = getenv("161f06fb88bab0de95ab10057555aaba")
BOT_USERNAME = getenv("BOT_USERNAME", "miwaamusic_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "saturn")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "haloisekai")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "suarakubot")
OWNER_NAME = getenv("OWNER_NAME", "ayannggmu") # isi dengan username kamu tanpa simbol @
DEV_NAME = getenv("DEV_NAME", "ayannggmu")
PMPERMIT = getenv("PMPERMIT", None)

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
