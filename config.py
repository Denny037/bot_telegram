import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
DESTINATION_CHANNEL = int(os.getenv("DESTINATION_CHANNEL"))

# Associa i canali ai rispettivi parser
SOURCE_CHANNELS = {
    -1001111111111: "parser_channel1",
    -1002222222222: "parser_channel2",
    -1003333333333: "parser_channel3"
}