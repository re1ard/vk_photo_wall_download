import vk_api
import urllib

api = vk_api.VkApi('login', 'pass')

count = (api.method('photos.get',{'owner_id':owner_id,'album_id':'wall','count':1,'offset':0})['count'] / 1000) + 1
owner_id = -64259879
i = 0

f = open(str(owner_id * -1),'w')

def give(offset):
	try:
		response=api.method('photos.get',{'owner_id':owner_id,'album_id':'wall','count':1000,'offset':offset})
		print str(offset) + '/' + str(count*1000)
		return response
	except Exception as msg:
		give(offset)


def photolink(data):
	if 'photo_1280' in data:
		return data['photo_1280']
	if 'photo_807' in data:
		return data['photo_807']
	if 'photo_604' in data:
		return data['photo_604']
	if 'photo_130' in data:
		return data['photo_130']
	if 'photo_75' in data:
		return data['photo_75']



while i<count:
	response=give(i*1000)
	for data in response['items']:
		f.write(photolink(data) + '\n')
		print photolink(data)
	i = i + 1

while 1:
	f.close()