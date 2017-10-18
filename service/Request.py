import hashlib
import hmac
import sys
import time

sys.path.insert(0, '')

import requests
from furl import furl

from data.Payload import Payload
from util import FileUtils
from util import constant

def getRequest(url):
    f = furl('%s' % url)
    f.args['apikey'] = constant.API_KEY
    f.args['nonce'] = time.time() * 1000
    signature = hmac.new(constant.SECRET_KEY.encode(), f.url.encode(), digestmod=hashlib.sha512)
    header = {constant.HEADER_APISIGN: signature, "Cache-Control": "no-cache", "Content-Type": "application/json"}
    return requests.get(f.url, headers=header)


#
# f = furl('%s' % constant.BASE_URL)
# # f.path = '/users/{user}'.format(user = "vuduychuong")
# f.path.add('/repos/{owner}/{repo}/pulls/{number}'.format(owner="framgia", repo="memvo_android", number=401))
# # f.url
# # payload = {'userId': '1', 'data': 1230}
# # header = {"Authorization": "token %s" % constant.TOKEN}
# # r = requests.get(url, params = payload)
# # r = requests.post(f.url, json = payload)
# r = requests.get(f.url, headers=header)
# pullRequest = payload.Payload(r.text)
# print(r.url)
# # print(r.text)
# print("lines addition: %s" % pullRequest.additions)
# print("lines detele: %s" % pullRequest.deletions)
# print("files changed: %s" % pullRequest.changed_files)

def getTicker():
    url = furl('%s' % constant.BASE_URL)
    url.path.add('/public/getmarkets')
    return getRequest(url.url)

    # r = requests.get(f.url, headers=header)
    # pullRequest = payload.Payload(r.text)
def getBalances():
    url = furl('%s' % constant.BASE_URL)
    url.path.add('/api/{version}'.format(version=constant.API_VERSION))
    # # url.path.add('/public/getmarkets')
    url.path.add('/account/getbalances')
    url.args['apikey'] = constant.API_KEY
    url.args['nonce'] = time.time() * 1000
    print(url.url)
    signature = hmac.new(constant.SECRET_KEY.encode(), url.url.encode(), digestmod=hashlib.sha512)
    header = {"%s" % constant.HEADER_APISIGN: "%s" % signature.hexdigest(), "Cache-Control": "no-cache",
              "Content-Type": "application/json"}
    # # r = requests.get(url.url)
    r = requests.get(url.url, headers=header)
    print(r.text)
    # data = {"changed_files": "3", "Wifi_1": -80}
    payload = Payload(r.text)
    FileUtils.appendFile("test.txt", repr(payload))
    print(FileUtils.readFile("test.txt"))
