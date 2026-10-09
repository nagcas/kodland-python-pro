# Bot su Discord — Kodland Corso Python Pro

## Obiettivo della lezione

In questa attività creeremo un semplice bot Discord con Python. Il bot potrà collegarsi a Discord, riconoscere un comando e rispondere con il risultato di una somma.

Al termine saprai:
- che cosa fa un bot Discord;
- a cosa serve il file `settings.py`;
- come funziona un comando con `commands.Bot`;
- come ricevere due numeri, sommarli e inviare il risultato nel canale.

---

## 1. Preparare il file `settings.py`

Nel progetto troverai il file di esempio `settings_esempio.py`.

1. Rinomina `settings_esempio.py` in `settings.py`.
2. Apri `settings.py`.
3. Inserisci nella chiave `TOKEN` il token del tuo bot, generato dal portale Discord Developer.

Esempio del contenuto del file:

```python
TOKEN = 'INCOLLA_QUI_IL_TOKEN_DEL_TUO_BOT'

