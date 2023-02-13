from pyrogram import Client, filters

app_id = ""
app_hash = ""

app = Client("my_account", app_id, app_hash)

@app.on_message(filters.me)
async def mes(client, message):
    return await editup(message)

@app.on_edited_message(filters.me)
async def edit(client, message):
    return await editup(message)
        
async def editup(message):
    print("yes")
    chat_id = -1
    
    if (message.chat.id==chat_id):
        mes_id = message.id
        message_text = message.text.upper()
        await app.edit_message_text(chat_id, mes_id, message_text)
    
    return

app.run()