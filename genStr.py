"""
Music Player, Telegram Voice Chat Bot
Session String Generator
"""

from pyrogram import Client

print("⚡ Telegram Pyrogram Session Generator ⚡\n")

api_id = int(input("👉 Enter your API ID: ").strip())
api_hash = input("👉 Enter your API HASH: ").strip()

print("\n✅ Login shuru ho gaya… (Telegram par code aayega)\n")

# Create Pyrogram Client & Export Session
with Client("genStr", api_id=api_id, api_hash=api_hash) as app:
    session = app.export_session_string()

print("🎉 SESSION STRING Successfully Generated!\n")
print("🔑 Your SESSION_STRING:\n")
print(session)
print("\n⚠️ Isse safe jagah rakhna — kisi ko mat dena!")
