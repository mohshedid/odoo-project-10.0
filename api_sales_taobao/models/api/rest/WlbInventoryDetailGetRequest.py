'''
Created by auto_sdk on 2016.01.25
'''
from base import RestApi
class WlbInventoryDetailGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.inventory_type_list = None
		self.item_id = None
		self.store_code = None

	def getapiname(self):
		return 'taobao.wlb.inventory.detail.get'
