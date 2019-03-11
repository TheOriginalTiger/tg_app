from telethon import TelegramClient, sync, events
from telethon.tl.types import User
import logging
from id_hash import info

id_ , h = info.info_() #get your app's id and hash on core.telegram.org 
client = TelegramClient('first_attempt', id_, h)

class dialog_():
	#all dialogs will be instances of this class
	#TODO establish a faster connection to get messages faster 
	def __init__(self, dia_obj):
		self.obj = 	dia_obj
		self.id_ = dia_obj.id
		self.hash = dia_obj.entity.access_hash
		self.messages = [] 
		for message in client.iter_messages(self.obj, limit = 10):
			self.messages.append(message.message)

	def __repr__(self):
		return "id {} hash {} messages {}".format(self.id_, self.hash, self.messages)

	#def get_messages(self):
	#	TODO this func is going to be used for getting messages from tg dialog so it can be placed in the app template
	#	pass
	#def send_message(self):
	#	TODO create a func for sending message 
	


@client.on(events.NewMessage)
async def my_event_handler(event):  
	sender = await event.get_sender()
	for obj in dia:
		# TODO adapt the whole func for db instead of class' list 
		if obj.id_ == sender.id and sender.id!=dia[-1].id_:
			obj.messages.append(event.message.message)
			
			
		

def start(client):	
	client.start()	
	logging.basicConfig(level=logging.ERROR)
	dia = getting_data(client)
	print(dia[-1])
	return dia

def getting_data(client):
	dialogs = client.get_dialogs()	
	dia = []
	for ent in dialogs:
		try:
			if type(ent.entity)==User:
				if ent.id == client.get_me().id:
					myself = dialog_(dia_obj =ent)
				else:
					obj = dialog_(dia_obj = ent )
					dia.append(obj)		
		except:
			pass
	dia.append(myself)	
	return dia
	


if __name__ == '__main__':		
	dia =start(client)
	#TODO create a disconnect func	
	client.run_until_disconnected()
	
		


		