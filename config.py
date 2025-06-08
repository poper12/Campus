env_vars = {
  # Get From my.telegram.org
  "API_HASH": "e9bfc473049cbaeff901ca6892d559c7",
  # Get From my.telegram.org
  "API_ID": "20373005",
  #Get For @BotFather
  "BOT_TOKEN": "7903390136:AAH8IL4ZajmK8MyQv8-nwEsU0xfZ3mWPLlA",
  # Get For tembo.io
  "DATABASE_URL_PRIMARY": "postgresql://neondb_owner:npg_NoDFHanE76qR@ep-twilight-fire-a80mx792-pooler.eastus2.azure.neon.tech/neondb?sslmode=require",
  # Logs Channel Username Without @
  "CACHE_CHANNEL": "Dump2075",
  # Force Subs Channel username without @
  "CHANNEL": "",
  # {chap_num}: Chapter Number
  # {chap_name} : Manga Name
  # Ex : Chapter {chap_num} {chap_name} @Manhwa_Arena
  "FNAME": "[MC] [{chap_num}] {chap_name} @Manga_Campus"  

}
dbname = env_vars.get('DATABASE_URL_PRIMARY') or env_vars.get('DATABASE_URL') or 'sqlite:///test.db'

if dbname.startswith('postgres://'):
    dbname = dbname.replace('postgres://', 'postgresql://', 1)
    
