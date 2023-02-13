from pyrogram import Client, filters

app_id = ""
app_hash = ""

app = Client("my_account", app_id, app_hash)

@app.on_message(filters.me)
async def mes(client, message):
    mes_id = message.id
    message_text = message.text.upper()
    chat_id = message.chat.id
    
    await app.edit_message_text(chat_id, mes_id, message_text)

app.run()