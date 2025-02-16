import logging

def simplify_message(original, channel_name):
    logging.info(f"Parsing messaggio per {channel_name} (Canale 3)")
    
    # Estrarre i dati secondo un formato differente
    lines = original.splitlines()
    entry = next((l.split()[1] for l in lines if "ENTRY" in l), None)
    sl = next((l.split()[1] for l in lines if "STOP" in l), None)
    tp = next((l.split()[1] for l in lines if "TARGET" in l), None)
    
    if not entry and not sl and not tp:
        logging.warning("Messaggio privo di dati significativi, ignorato.")
        return None
    
    formatted_message = f"Canale: {channel_name}\n\nENTRY: {entry}\nSTOP LOSS: {sl}\nTARGET: {tp}"
    
    return formatted_message