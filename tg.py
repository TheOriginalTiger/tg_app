from telethon import TelegramClient, sync, events
from telethon.tl.types import User
import logging
from id_hash import info

id_ , h = info.info_() #get your app's id and hash on core.telegram.org 
client = TelegramClient('first_attempt', id_, h)


@client.on(events.NewMessage)
async def my_event_handler(event):
	#TODO create a func to work with this data  
	sender = await event.get_sender()
	print(sender.first_name, ' says ', event.message.message )


def start(client):	
	client.start()	
	logging.basicConfig(level=logging.ERROR)
	keys = getting_data(client)
	return keys

def getting_data(client):
	dialogs = client.get_dialogs()	
	keys={}
	for ent in dialogs:
		try:
			if type(ent.entity)==User:
				keys.update({ent.id:ent.entity.access_hash})
		except:
			pass
	return keys


if __name__ == '__main__':		
	keys =start(client)
	#TODO create a disconnect func	
	client.run_until_disconnected()
	
		


		