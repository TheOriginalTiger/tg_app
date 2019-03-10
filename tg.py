from telethon import TelegramClient, sync, events
from telethon.tl.types import User
import logging
from id_hash import info

def start(id_, h):
	client = TelegramClient('first_attempt', id_, h)
	client.start()
	logging.basicConfig(level=logging.ERROR)
	keys = getting_data(client)
	


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
	id_ , h = info.info_() #get your app's id and hash on core.telegram.org 
	start(id_, h)
