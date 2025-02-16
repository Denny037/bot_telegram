import logging
from telethon import TelegramClient, events
from config import API_ID, API_HASH, SOURCE_CHANNELS, DESTINATION_CHANNEL
from parser_factory import get_parser

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

client = TelegramClient('session_name', API_ID, API_HASH)

@client.on(events.NewMessage(chats=list(SOURCE_CHANNELS.keys())))
async def handle_new_message(event):
    try:
        channel_id = event.chat_id
        parser = get_parser(SOURCE_CHANNELS[channel_id])
        
        if not parser:
            logging.warning(f"Nessun parser trovato per il canale {channel_id}. Messaggio ignorato.")
            return
        
        channel_name = event.chat.title if event.chat else "Sconosciuto"
        original_message = event.message.text
        
        if not original_message:
            logging.warning("Messaggio ricevuto vuoto o non testuale, ignorato.")
            return
        
        simplified_message = parser(original_message, channel_name)
        
        if simplified_message is None:
            return
        
        await client.send_message(DESTINATION_CHANNEL, simplified_message)
        logging.info("Messaggio inviato con successo.")
    
    except Exception as e:
        logging.error(f"Errore nel gestire il messaggio: {e}")

client.start()
logging.info("Bot avviato. In ascolto di nuovi messaggi...")
client.run_until_disconnected()