import logging

def simplify_message(original, channel_name):
    logging.info(f"Parsing messaggio per {channel_name} (Canale 1)")
    
    # Estrarre BUY/SELL, OPEN, SL, TP secondo la struttura del canale
    tipo = "BUY" if "BUY" in original.upper() else "SELL" if "SELL" in original.upper() else "Sconosciuto"
    
    # Estrarre dati con regex o split
    entry = next((line.split(":")[-1].strip() for line in original.splitlines() if "Open" in line), None)
    sl = next((line.split(":")[-1].strip() for line in original.splitlines() if "SL" in line), None)
    tp = next((line.split(":")[-1].strip() for line in original.splitlines() if "TP" in line), None)
    
    if not entry and not sl and not tp:
        logging.warning("Messaggio privo di dati significativi, ignorato.")
        return None
    
    formatted_message = f"Canale: {channel_name}\n\nTipo: {tipo}\nLivello di entrata: {entry}\nStop Loss: {sl}\nTake Profit: {tp}"
    
    return formatted_message