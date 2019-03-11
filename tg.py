from telethon import TelegramClient, sync, events
from telethon.tl.types import User
import logging
from id_hash import info

id_ , h = info.info_() #get your app's id and hash on core.telegram.org 
client = TelegramClient('first_attempt', id_, h)

class dialog_():
	#all dialogs will be instances of this class
	def __init__(self, id_, hash):
		self.id_ = id_
		self.hash = hash
		self.messages = []

	def __repr__(self):
		return "id {} hash {} mesagges {}".format(self.id_, self.hash, self.messages)

	#def get_messages(self):
	#	TODO this func is going to be used for getting messages from tg dialog so it can be placed in the app template
	#	pass


@client.on(events.NewMessage)
async def my_event_handler(event):  
	sender = await event.get_sender()
	#print(sender.first_name, ' says ', event.message.message )
	for obj in dia:
		# TODO adapt the whole func for db instead of class' list 
		if obj.id_ == sender.id and sender.id!=dia[-1].id:
			obj.messages.append(event.message.message)
			
		

def start(client):	
	client.start()	
	logging.basicConfig(level=logging.ERROR)
	dia = getting_data(client)
	return dia

def getting_data(client):
	dialogs = client.get_dialogs()	
	dia = []
	for ent in dialogs:
		try:
			if type(ent.entity)==User:
				if ent.id == client.get_me().id:
					myself = client.get_me()
				else:
					obj = dialog_(id_ =ent.id, hash= ent.entity.access_hash )
					dia.append(obj)		
		except:
			pass
	dia.append(myself)	
	return dia


if __name__ == '__main__':		
	dia =start(client)
	#TODO create a disconnect func	
	client.run_until_disconnected()
	
		


		