from telethon import TelegramClient, sync, events
from telethon.tl.types import User
import logging
from id_hash import info
#import socks

id_ , h = info.info_() #get your app's id and hash on core.telegram.org 
client = TelegramClient('first_attempt', id_, h) #, proxy=(socks.SOCKS4, '198.50.177.44', 44699) )

class dialog_():	
	def __init__(self, dia_obj):
		self.obj = 	dia_obj
		self.id_ = dia_obj.id
		self.hash = dia_obj.entity.access_hash
		self.name = self.obj.name
		self.messages = [] 
		self.senders = []
		user = client.get_me()
		for message in client.iter_messages(self.obj, limit = 10):	
			self.messages.append(message.message)
			if self.obj.id != client.get_me().id:
				if message.sender.last_name: 
					self.senders.append(str(message.sender.first_name + ' ' + message.sender.last_name))
				else:
					self.senders.append(message.sender.first_name)
			else:
				if user.last_name:
					self.senders.append(user.first_name + ' ' + user.last_name)
				else:
					self.senders.append(user.first.name)		
		self.messages.reverse()
		if self.obj.id != client.get_me().id:
			self.senders.reverse()

	def __repr__(self):
		return "id {} hash {} messages {} senders{}".format(self.id_, self.hash, self.messages, self.senders)
 


	#def get_messages(self):
	#	TODO this func is going to be used for getting messages from tg dialog so it can be placed in the app template
	#	pass
	#def send_message(self):
	#	TODO create a func for sending message 
	

#with method
@client.on(events.NewMessage)
async def my_event_handler(event):
	chat_user_id = event.message.to_id.user_id
	endpoint_id = None
	sender = await event.get_sender()
	if chat_user_id == dia[-1].id_:
		endpoint_id = sender.id
	else : 
		endpoint_id = chat_user_id
	i = 0

	for obj in dia:
		# TODO adapt the whole func for db instead of class' list 
		
		if obj.id_ == endpoint_id:# and sender.id!=dia[-1].id_:
			obj.messages.append(event.message.message)
			kek = obj.messages
			rofl = i 
		i+=1
	try:
		print(dia[-1].messages)		
	except:
		pass		
		

def start(client):	
	client.start(max_attempts = 1)
	logging.basicConfig(level=logging.ERROR)
	dia = getting_data(client)
	return dia

def getting_data(client):
	dialogs = client.get_dialogs()	
	dia = []
	for ent in dialogs:
		try:
			if type(ent.entity) == User:
				if ent.id == client.get_me().id:					
					myself = dialog_(dia_obj = ent)
				else:
					obj = dialog_(dia_obj = ent )
					dia.append(obj)		
		except:
			pass
	dia.append(myself)	
	return dia
	


if __name__ == '__main__':			
	dia =start(client)	
	print(dia[-1].id_)
	#TODO create a disconnect func	
	client.disconnect()
	print('done')
	

	#print(dir(client.iter_messages(dia[0].obj, limit=1)))
	
		


		