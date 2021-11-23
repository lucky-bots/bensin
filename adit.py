# -*- coding: utf-8 -*- 
import LINEPY
from LINEPY import *
from akad.ttypes import *
#from thrift.unverting import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, ctypes, urllib, wikipedia
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup
#import pyimgflip
#from googletrans import Translator
import youtube_dl

aditmadzs = LineClient("adirekpanyade@gmail.com","Aa1234")
#aditmadzs = LineClient(authToken='token')
aditmadzs.log("Auth Token : " + str(aditmadzs.authToken))
channel = LineChannel(aditmadzs)
aditmadzs.log("Channel Access Token : " + str(channel.channelAccessToken))

ki = LineClient("hujj488@gmail.com","Aa1234")
#ki = LineClient(authToken='Token')
ki.log("Auth Token : " + str(ki.authToken))
channel1 = LineChannel(ki)
ki.log("Channel Access Token : " + str(channel1.channelAccessToken))

#ubah mid di dalem admin,owner,creator.json dengan mid kalian
poll = LinePoll(aditmadzs)
call = aditmadzs
creator = ["ue8d4c133178ae5a305354ddc71b1e577"]
owner = ["ue8d4c133178ae5a305354ddc71b1e577"]
admin = ["ue8d4c133178ae5a305354ddc71b1e577"]
staff = ["ue8d4c133178ae5a305354ddc71b1e577"]
mid = aditmadzs.getProfile().mid
Amid = ki.getProfile().mid
KAC = [aditmadzs,ki]
ABC = [ki]
Bots = [mid,Amid]
Aditmadzs = admin + staff

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []

welcome = []
#simisimi = []
#translateen = []
#translateid = []
#translateth = []
#translatetw = []
#translatear = []

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

aditProfile = aditmadzs.getProfile()
myProfile["displayName"] = aditProfile.displayName
myProfile["statusMessage"] = aditProfile.statusMessage
myProfile["pictureStatus"] = aditProfile.pictureStatus

responsename1 = ki.getProfile().displayName

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)
with open('admin.json', 'r') as fp:
    admin = json.load(fp)    

Setbot1 = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot1)
Setbot2 = codecs.open("settings.json","r","utf-8")
settings = json.load(Setbot2)
Setbot3 = codecs.open("wait.json","r","utf-8")
wait = json.load(Setbot3)
Setbot4 = codecs.open("read.json","r","utf-8")
read = json.load(Setbot4)

mulai = time.time()

msg_dict = {}
msg_dict1 = {}

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
    
    
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def backupData():
    try:
        backup1 = Setmain
        f = codecs.open('setting.json','w','utf-8')
        json.dump(backup1, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup2 = settings
        f = codecs.open('settings.json','w','utf-8')
        json.dump(backup2, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup3 = wait
        f = codecs.open('wait.json','w','utf-8')
        json.dump(backup3, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup4 = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup4, f, sort_keys=True, indent=4, ensure_ascii=False)        
        return True
    except Exception as error:
        logError(error)
        return False     

def restartBot():
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Mention User「{}」\n\n  [ Mention ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(aditmadzs.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        aditmadzs.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "พบสมาชิก {} คน \nคุณ ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(aditmadzs.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        aditmadzs.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "สมาชิกใหม { }\nสวัสดีครับคุณ  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = aditmadzs.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nDi group "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(aditmadzs.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        aditmadzs.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Member Keluar「{}」\nByee  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = aditmadzs.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E' :elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["leave"]+"\nDari group "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(aditmadzs.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        aditmadzs.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))        

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:slen, 'E' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:elen, 'M' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = aditmadzs.getAllContactIds()
        gid = aditmadzs.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"◐ Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\n🐚 Group : "+str(len(gid))+"\n🐚 Teman : "+str(len(teman))+"\n🐚 Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n🐚 Runtime : \n • "+bot
        aditmadzs.sendMessage(to, text, {'MENTION' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']: str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = ""
    return helpMessage
    
    

def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = ""
    return helpMessage2
    
def translate():
    helpTranslate =    ""
    return helpTranslate

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if aditmadzs.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            aditmadzs.reissueGroupTicket(op.param1)
                            X = aditmadzs.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            aditmadzs.updateGroup(X)
                            aditmadzs.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    try:
                        if ki.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                ki.reissueGroupTicket(op.param1)
                                X = ki.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                ki.updateGroup(X)
                                aditmadzs.sendMessage(op.param1, None, contentMetadata={'mid' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']: op.param2}, contentType=13)
                    except:
                        pass
                                                
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        aditmadzs.acceptGroupInvitation(op.param1)
                        ginfo = aditmadzs.getGroup(op.param1)
                        aditmadzs.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        aditmadzs.leaveGroup(op.param1)
                    else:
                        aditmadzs.acceptGroupInvitation(op.param1)
                        ginfo = aditmadzs.getGroup(op.param1)
                        aditmadzs.sendMessage(op.param1,"Hai " + str(ginfo.name))

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        aditmadzs.acceptGroupInvitation(op.param1)
                        ginfo = aditmadzs.getGroup(op.param1)
                        aditmadzs.sendMessage(op.param1,"สวัสดีครับคุณ, salken yaa ^^")
                    else:
                        aditmadzs.acceptGroupInvitation(op.param1)
                        ginfo = aditmadzs.getGroup(op.param1)
                        aditmadzs.sendMessage(op.param1,"สวัสดีครับคุณ, salken yaa ^^")
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        ki.leaveGroup(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Hai " + str(ginfo.name))

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = aditmadzs.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            random.choice(KAC).cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = ki.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                random.choice(KAC).cancelGroupInvitation(op.param1,[_mid])
                        except:
                            pass

        if op.type == 15:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = aditmadzs.getGroup(op.param1)
                contact = aditmadzs.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                leaveMembers(op.param1, [op.param2])
                aditmadzs.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = aditmadzs.getGroup(op.param1)
                contact = aditmadzs.getContact(op.param2)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                welcomeMembers(op.param1, [op.param2])
                aditmadzs.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                return

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        aditmadzs.sendMessage(op.param1, wait["message"])

#===========KICK============#
        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
                
#===========Cancel============#

        if op.type == 32:
            if op.param1 in protectcancel:
              if op.param3 in Bots:    
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            ki.findAndAddContactsByMid(op.param1,[Zmid])
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[Zmid])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                aditmadzs.findAndAddContactsByMid(op.param1,[Zmid])
                                aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                                aditmadzs.inviteIntoGroup(op.param1,[Zmid])
                        except:
                            pass
                return

        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        aditmadzs.acceptGroupInvitation(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            G = ki.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            G = ki.getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                        except:
                            pass
                return

            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        aditmadzs.inviteIntoGroup(op.param1,[op.param3])
                        ki.acceptGroupInvitation(op.param1)
                        aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            G = aditmadzs.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            aditmadzs.updateGroup(G)
                            Ticket = aditmadzs.reissueGroupTicket(op.param1)
                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                            aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                            G = aditmadzs.getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            aditmadzs.updateGroup(G)
                            Ticket = aditmadzs.reissueGroupTicket(op.param1)
                        except:
                            pass
                return


            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.findAndAddContactsByMid(op.param1,admin)
                        ki.inviteIntoGroup(op.param1,admin)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            aditmadzs.findAndAddContactsByMid(op.param1,admin)
                            aditmadzs.inviteIntoGroup(op.param1,admin)
                            aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass

                return

            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.findAndAddContactsByMid(op.param1,staff)
                        ki.inviteIntoGroup(op.param1,staff)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            aditmadzs.findAndAddContactsByMid(op.param1,staff)
                            aditmadzs.inviteIntoGroup(op.param1,staff)
                            aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass

                return

        if op.type == 55:
            try:
                if op.param1 in Setmain["ADITMADZSreadPoint"]:
                   if op.param2 in Setmain["ADITMADZSreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["ADITMADZSreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = aditmadzs.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
     #                   contact = aditmadzs.getContact(op.param2)
          #              image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        aditmadzs.sendImageWithURL(op.param1, image)                        
                        
                    
        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = aditmadzs.getGroup(at)
                                Aditmadzs = aditmadzs.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Gambar Dihapus 」\n• Pengirim : "
                                ret_ = "• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(Aditmadzs.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':Aditmadzs.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                aditmadzs.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                aditmadzs.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = aditmadzs.getGroup(at)
                                Aditmadzs = aditmadzs.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 Pesan Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(Aditmadzs.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n• Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                aditmadzs.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = aditmadzs.getGroup(at)
                                Aditmadzs = aditmadzs.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "「 Sticker Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(Aditmadzs.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                aditmadzs.sendMessage(at, str(ret_))
                                aditmadzs.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)

                    

        

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 0:
                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                
            if msg.contentType == 1:
                    path = aditmadzs.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
            if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n「 Sticker Info 」"
                   ret_ += "\n• Sticker ID : {}".format(stk_id)
                   ret_ += "\n• Sticker Version : {}".format(stk_ver)
                   ret_ += "\n• Sticker Package : {}".format(pkg_id)
                   ret_ += "\n• Sticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = aditmadzs.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
                                                      
                            
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    aditmadzs.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    aditmadzs.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = aditmadzs.getContact(msg.contentMetadata["mid"])
                        path = aditmadzs.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        aditmadzs.sendMessage(msg.to,"⏩ Nama : " + msg.contentMetadata["displayName"] + "\n⏩ MID : " + msg.contentMetadata["mid"] + "\n⏩ Status : " + contact.statusMessage + "\n⏩ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        aditmadzs.sendImageWithURL(msg.to, image)
#===========ADD BOT============#
               if msg.contentType == 13:
                 #if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        aditmadzs.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        aditmadzs.sendMessage(msg.to,"Berhasil menambahkan ke anggota bot")
         
                  if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        aditmadzs.sendMessage(msg.to,"Berhasil menghapus dari anggota bot")
                    else:
                        wait["dellbots"] = True
                        aditmadzs.sendMessage(msg.to,"Contact itu bukan anggota Aditmadzs BOT")
#===========ADD STAFF============#
                 #if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        aditmadzs.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        aditmadzs.sendMessage(msg.to,"Berhasil menambahkan ke staff")
                  if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        aditmadzs.sendMessage(msg.to,"Berhasil menghapus dari staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        aditmadzs.sendMessage(msg.to,"Contact itu bukan staff")
#===========ADD ADMIN============#
                 #if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        aditmadzs.sendMessage(msg.to,"Contact itu sudah jadi admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        aditmadzs.sendMessage(msg.to,"Berhasil menambahkan ke admin")
                  if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        aditmadzs.sendMessage(msg.to,"Berhasil menghapus dari admin")
                    else:
                        wait["delladmin"] = True
                        aditmadzs.sendMessage(msg.to,"Contact itu bukan admin")
#===========ADD BLACKLIST============#

#===========UPDATE FOTO============#
               if msg.contentType == 1:
                 #if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = aditmadzs.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            aditmadzs.sendMessage(msg.to, "Berhasil menambahkan gambar")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 #if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = aditmadzs.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     aditmadzs.updateGroupPicture(msg.to, path)
                     aditmadzs.sendMessage(msg.to, "Berhasil mengubah foto group")

               if msg.contentType == 1:
                   #if msg._from in admin:
                       if mid in Setmain["ADITMADZSfoto"]:
                            path = aditmadzs.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][mid]
                            aditmadzs.updateProfilePicture(path)
                            aditmadzs.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 #if msg._from in admin:
                        if Amid in Setmain["ADITMADZSfoto"]:
                            path = ki.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Amid]
                            ki.updateProfilePicture(path)
                            ki.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 #if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = ki.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     ki.updateProfilePicture(path1)
                     ki.sendMessage(msg.to, "Berhasil mengubah foto profile bot")               

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        aditmadzs.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help" and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                               helpMessage = help()
                               aditmadzs.sendMessage(msg.to, str(helpMessage))
                                                               
                        if cmd == "self on" and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                            #if msg._from in admin:
                                wait["selfbot"] = True
                                aditmadzs.sendMessage(msg.to, "Selfbot diaktifkan")
                                
                        if cmd == "self off" and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                            #if msg._from in admin:
                                wait["selfbot"] = False
                                aditmadzs.sendMessage(msg.to, "Selfbot dinonaktifkan")
                                            
                        elif cmd == "คำสั่งบอท" and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                               helpMessage1 = helpbot()
                               aditmadzs.sendMessage(msg.to, str(helpMessage1))
                               
                        elif cmd == "คำสั่ง2" and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                               helpMessage2 = infomeme()
                               aditmadzs.sendMessage(msg.to, str(helpMessage2))
                               
                        elif cmd == "translate" and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                               helpTranslate = translate()
                               aditmadzs.sendMessage(msg.to, str(helpTranslate))             
                               
            

                        elif cmd == "creator" or text.lower() == 'creator' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                            #if msg._from in admin:
                                aditmadzs.sendMessage(msg.to,"ผู้สร้างบอท") 
                                ma = ""
                                for i in creator:
                                    ma = aditmadzs.getContact(i)
                                    aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "about" or cmd == "informasi":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                               sendMention(msg.to, sender, "「 ◄]·❍✯͜͡⊰์◉⊱τ∉∂m d®∂ⓖ๏n ❂Ғ w∂®®¡๏®⊰์◉⊱™️✯͜͡❂➣ SelfBOT 1 Assist 」\n")
                               aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == "ฉัน" or text.lower() == 'ฉัน' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': msg._from}
                               aditmadzs.sendMessage(msg)

                        elif text.lower() == "มิดฉัน" and sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                            #if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, msg._from)

                        elif ("มิด " in msg.text):
                           if sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                               if wait["selfbot"] == True:
                            #if msg._from in admin:
                                  key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = aditmadzs.getContact(key1)
                               aditmadzs.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = aditmadzs.getContact(key1)
                               aditmadzs.sendMessage(msg.to, "❧ Nama : "+str(mi.displayName)+"\n🐚 Mid : " +key1+"\n🐚 Status : "+str(mi.statusMessage))
                               aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(aditmadzs.getContact(key1)):
                                   aditmadzs.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   aditmadzs.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "บอท" and sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                           if wait["selfbot"] == True:
                            #if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               aditmadzs.sendMessage(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Amid}
                               aditmadzs.sendMessage1(msg)

                        elif text.lower() == "ลบแชท" and sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                           if wait["selfbot"] == True:
                            #if msg._from in admin:
                               try:
                                   aditmadzs.removeAllMessages(op.param2)
                               except:
                                   pass

                        elif text.lower() == "ลบ" and sender in ['ue8d4c133178ae5a305354ddc71b1e577']: 
                           if wait["selfbot"] == True:
                            #if msg._from in admin:
                               try:
                                   ki.removeAllMessages(op.param2)
                                   aditmadzs.sendMessage(msg.to,"Chat dibersihkan...")
                               except:
                                   pass

                        elif cmd.startswith("broadcast: "):
                           if  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                             if wait["selfbot"] == True:
                            #if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = aditmadzs.getGroupIdsJoined()
                               for group in saya:
                                   aditmadzs.sendMessage(group,"=======[BROADCAST]=======\n\n"+pesan+"\n\nCreator : line.me/ti/p/~mostarz\n\nChannel Youtube : https://youtu.be/cmVxZyKCrxE")

                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "「Mykey」\nSetkey bot mu「 " + str(Setmain["keyCommand"]) + " 」")
                               
                        elif cmd.startswith("setkey "):
                           if  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                             if wait["selfbot"] == True:
                            #if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   aditmadzs.sendMessage(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   aditmadzs.sendMessage(msg.to, "「Setkey」\nSetkey diganti jadi「{}」".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               aditmadzs.sendMessage(msg.to, "「Setkey」\nSetkey mu kembali ke awal")

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               aditmadzs.sendMessage(msg.to, "Restart Sukses Bos!...")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                            
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Aktif " +waktu(eltime)
                               aditmadzs.sendMessage(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          #if msg._from in admin:
                            try:
                                G = aditmadzs.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(aditmadzs.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                aditmadzs.sendMessage(msg.to, "❧ BOT Grup Info\n\n ❧ Nama Group : {}".format(G.name)+ "\n🐚 ID Group : {}".format(G.id)+ "\n🐚 Pembuat : {}".format(G.creator.displayName)+ "\n🐚 Waktu Dibuat : {}".format(str(timeCreated))+ "\n🐚 Jumlah Member : {}".format(str(len(G.members)))+ "\n🐚 Jumlah Pending : {}".format(gPending)+ "\n🐚 Group Qr : {}".format(gQr)+ "\n🐚 Group Ticket : {}".format(gTicket))
                                aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                aditmadzs.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                aditmadzs.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                           if  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          #if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = aditmadzs.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = aditmadzs.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(aditmadzs.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "⏩ BOT Grup Info\n"
                                ret_ += "\n⏩ Name : {}".format(G.name)
                                ret_ += "\n⏩ ID : {}".format(G.id)
                                ret_ += "\n⏩ Creator : {}".format(gCreator)
                                ret_ += "\n⏩ Created Time : {}".format(str(timeCreated))
                                ret_ += "\n⏩ Member : {}".format(str(len(G.members)))
                                ret_ += "\n⏩ Pending : {}".format(gPending)
                                ret_ += "\n⏩ Qr : {}".format(gQr)
                                ret_ += "\n⏩ Ticket : {}".format(gTicket)
                                ret_ += ""
                                aditmadzs.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                           if  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          #if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = aditmadzs.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = aditmadzs.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "⏩ "+ str(no) + ". " + mem.displayName
                                aditmadzs.sendMessage(to,"⏩ Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("leave: "):
                           if  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          #if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = aditmadzs.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = aditmadzs.getGroup(i)
                                if ginfo == group:
                                    ki.leaveGroup(i)
                                    aditmadzs.sendMessage(msg.to,"Berhasil keluar di grup " +str(ginfo.name))

                        elif cmd == "fiendlist":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = aditmadzs.getAllContactIds()
                               for i in gid:
                                   G = aditmadzs.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.displayName+ "\n"
                               aditmadzs.sendMessage(msg.to,"┏━━[ FRIEND LIST ]\n┃┃\n"+ma+"┃┃\n┗━━[ Total「"+str(len(gid))+"」Friends ]")

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = aditmadzs.getGroupIdsJoined()
                               for i in gid:
                                   G = aditmadzs.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.name+ "\n"
                               aditmadzs.sendMessage(msg.to,"┏━━[ GROUP LIST ]\n┃┃\n"+ma+"┃┃\n┗━━[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist1":
                            #if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = ki.getGroupIdsJoined()
                               for i in gid:
                                   G = ki.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.name+ "\n"
                               ki.sendMessage(msg.to,"┏━━[ GROUP LIST ]\n┃┃\n"+ma+"┃┃\n┗━━[ Total「"+str(len(gid))+"」Groups ]")


                        elif cmd == "open":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                if msg.toType == 2:
                                   X = ki.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   ki.updateGroup(X)
                                   ki.sendMessage(msg.to, "Url Opened")

                        elif cmd == "close":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                if msg.toType == 2:
                                   X = ki.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   ki.updateGroup(X)
                                   ki.sendMessage(msg.to, "Url Closed")

                        elif cmd == "url grup":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                if msg.toType == 2:
                                   x = ki.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      ki.updateGroup(x)
                                   gurl = ki.reissueGroupTicket(msg.to)
                                   ki.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)
                                   
                                   
                        elif cmd == "reject":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                              ginvited = aditmadzs.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      aditmadzs.rejectGroupInvitation(gid)
                                  aditmadzs.sendMessage(to, "Berhasil tolak sebanyak {} undangan grup".format(str(len(ginvited))))
                              else:
                                  aditmadzs.sendMessage(to, "Tidak ada undangan yang tertunda")

#===========BOT UPDATE============#
                        elif cmd == "updategrup":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                aditmadzs.sendMessage(msg.to,"Kirim fotonya.....")

                        elif cmd == "updatebot":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                settings["changePicture"] = True
                                ki.sendMessage(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "updatefoto":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                Setmain["ADITMADZSfoto"][mid] = True
                                aditmadzs.sendMessage(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot1up":
                            #if msg._from in admin:
                                Setmain["ADITMADZSfoto"][Amid] = True
                                ki.sendMessage(msg.to,"Kirim fotonya.....")
                               

                        elif cmd.startswith("myname: "):
                           if  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          #if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = aditmadzs.getProfile()
                                profile.displayName = string
                                aditmadzs.updateProfile(profile)
                                aditmadzs.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot1name: "):
                           if  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          #if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ki.getProfile()
                                profile.displayName = string
                                ki.updateProfile(profile)
                                ki.sendMessage(msg.to,"Nama diganti jadi " + string + "")

#===========BOT UPDATE============#
                        elif cmd == "แทค" or text.lower() == '😆' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          if wait["selfbot"] == True:
                               group = aditmadzs.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4, jml = [], [], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (80, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm4)

                        elif cmd == "listbot":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +aditmadzs.getContact(m_id).displayName + "\n"
                                aditmadzs.sendMessage(msg.to,"⏩ BOT\n\n"+ma+"\nTotal「%s」BOT" %(str(len(Bots))))

                        elif cmd == "listadmin":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +aditmadzs.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +aditmadzs.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +aditmadzs.getContact(m_id).displayName + "\n"
                                aditmadzs.sendMessage(msg.to,"⏩ Admin Aditmadzs BOT\n\n⏩Creator BOT:\n"+ma+"\n⏩Admin:\n"+mb+"\n⏩Staff:\n"+mc+"\n⏩Total「%s」" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "listprotect":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                me = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                e = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +aditmadzs.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +aditmadzs.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +aditmadzs.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +aditmadzs.getGroup(group).name + "\n"
                                gid = protectinvite
                                for group in gid:
                                    e = e + 1
                                    end = '\n'
                                    me += str(e) + ". " +aditmadzs.getGroup(group).name + "\n"                                    
                                aditmadzs.sendMessage(msg.to,"⏩ BOT Protection\n\n⏩ PROTECT URL :\n"+ma+"\n⏩ PROTECT KICK :\n"+mb+"\n⏩ PROTECT JOIN :\n"+md+"\n⏩ PROTECT CANCEL:\n"+mc+"\n⏩ PROTECT INVITE :\n"+me+"\nTotal「%s」Protect yang aktif" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel)+len(protectinvite))))

                        elif cmd == "respon":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                ki.sendMessage(msg.to,responsename1)

                        elif cmd == "มา" and sender in ['ue8d4c133178ae5a305354ddc71b1e577']: 
                            if wait["selfbot"] == True:
                            #if msg._from in admin:
                                try:
                                    anggota = [Amid]
                                    aditmadzs.inviteIntoGroup(msg.to, anggota)
                                    ki.acceptGroupInvitation(msg.to)
                                except:
                                    pass
                                
    
                        elif cmd == "/มา" and sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                            if wait["selfbot"] == True:
                            #if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = gg.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)

                        elif cmd == "/บาย":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ki.sendMessage(msg.to, "Bye bye group "+str(G.name))
                                ki.leaveGroup(msg.to)
                                

                        elif cmd.startswith("leave "):
                           if  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                            #if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = aditmadzs.getGroupIdsJoined()
                                for i in gid:
                                    h = aditmadzs.getGroup(i).name
                                    if h == ng:
                                        ki.sendMessage(i, "Silahkan admin invite atau masukan kembali")
                                        ki.leaveGroup(i)
                                        aditmadzs.sendMessage(to,"Berhasil keluar dari grup " +h)

                        elif cmd == "/มาา":
                            #if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)


                        elif cmd == "sprespon":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = aditmadzs.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = aditmadzs.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = aditmadzs.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                aditmadzs.sendMessage(msg.to, " ❧ BOT Speed respon\n\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                               start = time.time()
                               aditmadzs.sendMessage(msg.to, "Progres speed...")
                               elapsed_time = time.time() - start
                               aditmadzs.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))

                        elif cmd == "lurking on":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['ADITMADZSreadPoint'][msg.to] = msg_id
                                 Setmain['ADITMADZSreadMember'][msg.to] = {}
                                 aditmadzs.sendMessage(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurking off":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['ADITMADZSreadPoint'][msg.to]
                                 del Setmain['ADITMADZSreadMember'][msg.to]
                                 aditmadzs.sendMessage(msg.to, "Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurkers":
                          #if msg._from in admin:
                            if msg.to in Setmain['ADITMADZSreadPoint']:
                                if Setmain['ADITMADZSreadMember'][msg.to] != {}:
                                    nad = []
                                    for x in Setmain['ADITMADZSreadMember'][msg.to]:
                                        nad.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Lurkers ]\n1. ".format(str(len(nad)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in nad:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(nad):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(aditmadzs.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        aditmadzs.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['ADITMADZSreadPoint'][msg.to]
                                        del Setmain['ADITMADZSreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['ADITMADZSreadPoint'][msg.to] = msg.id
                                    Setmain['ADITMADZSreadMember'][msg.to] = {}
                                else:
                                    aditmadzs.sendMessage(msg.to, "User kosong...")
                            else:
                                aditmadzs.sendMessage(msg.to, "Ketik lurking on dulu")

                        elif cmd == "อ่าน" and sender in ['ue8d4c133178ae5a305354ddc71b1e577']: 
                           if wait["selfbot"] == True:
                           #if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  aditmadzs.sendMessage(msg.to, "เปิดระบบเช็คคนอ่าน\nวันที่ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n,กลุ่ม [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "ปิดอ่าน":
                          if wait["selfbot"] == True:
                           #if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  aditmadzs.sendMessage(msg.to, "ระบบเช็คคนอ่าน\n\n : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  aditmadzs.sendMessage(msg.to, "Sudak tidak aktif")

#===========Hiburan============#
                                      
                        elif cmd.startswith("musik: "):
                           if  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          #if msg._from in admin:    
                            try:
                                search = msg.text.replace("musik: ","")
                                r = requests.get("https://farzain.xyz/api/premium/joox.php?apikey=al11241519&id={}".format(urllib.parse.quote(search)))
                                data = r.text
                                data = json.loads(data)
                                info = data["info"]
                                audio = data["audio"]
                                hasil = "「 Hasil Musik 」\n"
                                hasil += "\nPenyanyi : {}".format(str(info["penyanyi"]))
                                hasil += "\nJudul : {}".format(str(info["judul"]))
                                hasil += "\nAlbum : {}".format(str(info["album"]))
                                hasil += "\n\nLink : \n1. Image : {}".format(str(data["gambar"]))
                                hasil += "\n\nLink : \n2. MP3 : {}".format(str(audio["mp3"]))
                                hasil += "\n\nLink : \n3. M4A : {}".format(str(audio["m4a"]))
                                aditmadzs.sendImageWithURL(msg.to, str(data["gambar"]))
                                aditmadzs.sendMessage(msg.to, str(hasil))
                                aditmadzs.sendMessage(msg.to, "Downloading...")
                                aditmadzs.sendMessage(msg.to, "「 Result MP3 」")
                                aditmadzs.sendAudioWithURL(msg.to, str(audio["mp3"]))
                                aditmadzs.sendMessage(msg.to, "「 Result M4A 」")
                                aditmadzs.sendVideoWithURL(msg.to, str(audio["m4a"]))
                                aditmadzs.sendMessage(msg.to, str(data["lirik"]))
                                aditmadzs.sendMessage(msg.to, "Success Download...")
                            except Exception as error:
                            	aditmadzs.sendMessage(msg.to, "「 Result Error 」\n" + str(error))

                        elif cmd.startswith("randomnumber: "):
                           if  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:                            	
                            #if msg._from in admin:
                                separate = msg.text.split(" ")
                                angka = msg.text.replace(separate[0] + " ","")  
                                tgb = angka.split("-")
                                num1 = tgb[0]
                                num2 = tgb[1]
                                r = requests.get("https://farzain.xyz/api/random.php?min="+num1+"&max="+num2)
                                data = r.json()
                                aditmadzs.sendMessage(msg.to,"Hasil : "+str(data["url"]))
                                
                                
                        elif cmd.startswith("1cak"):
                           if  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          #if msg._from in admin:
                              r=requests.get("https://api-1cak.herokuapp.com/random")
                              data=r.text
                              data=json.loads(data)
                              print(data)
                              hasil = "Result :\n"
                              hasil += "\nID : " +str(data["id"])
                              hasil += "\nTitle : " + str(data["title"])
                              hasil += "\nUrl : " + str(data["url"]) 
                              hasil += "\nVotes : " + str(data["votes"])
                              aditmadzs.sendMessage(msg.to, str(hasil))
        
                        elif cmd.startswith("musik2: "):
                           if  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          #if msg._from in admin:    
                            try:
                                dan = msg.text.replace("musik2: ","")
                                r = requests.get("http://corrykalam.pw/api/joox.php?song={}"+urllib.parse.quote(dan))
                                data = r.json()
                                l = data["lyric"].replace("ti:","Judul: ")
                                i = l.replace("ar:","Penyanyi: ")
                                r = i.replace("al:","Album: ")
                                ii = r.replace("[by:]","")
                                k = ii.replace("[offset:0]","")
                                lirik = k.replace("***Lirik didapat dari pihak ketiga***\n","")
                                aditmadzs.sendImageWithURL(msg.to, data["image"])
                                t = "[ Music ]"
                                t += "\n\nJudul: "+str(data["title"])
                                t+="\nPenyanyi: "+str(data["singer"])
                                t+="\n\n[ Finish ]\n\n"+str(lirik)
                                aditmadzs.sendMessage(msg.to, str(t))
                                aditmadzs.sendAudioWithURL(msg.to, data["url"])
                            except Exception as error:
                                pass
                            
                        elif cmd.startswith("playlist "):
                           if  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          #if msg._from in admin:    
                            try:
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split(":")
                                search = str(cond[0])
                                result = requests.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "━━━━[ List Lagu ]━━━━"
                                    for music in data["result"]:
                                        num += 1
                                        ret_ += "\n {}. {}".format(str(num), str(music["single"]))
                                    ret_ += "\n  ━━[ Total {} Lagu ]━━".format(str(len(data["result"])))
                                    ret_ += "\n\nUntuk Melihat Details Musik, Silahkan Ketik \n❧「 {}Playlist {}:nomor 」 ".format(str(),str(search))
                                    ret_ += "\n❧「 {}Lirik {}:nomor 」 ".format(str(),str(search))
                                    aditmadzs.sendMessage(msg.to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["result"]):
                                        music = data["result"][num - 1]
                                        result = requests.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                        data = result.text
                                        data = json.loads(data)
                                        if data["result"] != []:
                                            ret_ = "┏━━━━[ Detail Musik ]━━━━"
                                            ret_ += "\n┃┃ Title : {}".format(str(data["result"]["song"]))
                                            ret_ += "\n┃┃ Album : {}".format(str(data["result"]["album"]))
                                            ret_ += "\n┃┃ Size : {}".format(str(data["result"]["size"]))
                                            ret_ += "\n┗━━[ Tunggu Audionya ]━━━"
                                            aditmadzs.sendMessage(msg.to, str(ret_))
                                            aditmadzs.sendAudioWithURL(msg.to, str(data["result"]["mp3"][0]))
                            except Exception as error:
                                pass
                            
                        elif cmd.startswith("lirik "):
                           if  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          #if msg._from in admin:    
                            try:
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split(":")
                                search = cond[0]
                                api = requests.get("http://api.secold.com/joox/cari/{}".format(str(search)))
                                data = api.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "━━━━[ List Lirik ]━━━━"
                                    for lyric in data["results"]:
                                        num += 1
                                        ret_ += "\n {}. {}".format(str(num), str(lyric["single"]))
                                    ret_ += "\n  ━━[ Total {} Lagu ]━━".format(str(len(data["results"])))
                                    ret_ += "\n\nUntuk Melihat Details Musik, Silahkan Ketik \n❧「 {}Lirik {}:nomor 」".format(str(),str(search))
                                    ret_ += "\n❧「 {}Playlist {}:nomor 」 ".format(str(),str(search))
                                    aditmadzs.sendMessage(msg.to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["results"]):
                                        lyric = data["results"][num - 1]
                                        api = requests.get("http://api.secold.com/joox/sid/{}".format(str(lyric["songid"])))
                                        data = api.text
                                        data = json.loads(data)
                                        lyrics = data["results"]["lyric"]
                                        lyric = lyrics.replace('ti:','Title - ')
                                        lyric = lyric.replace('ar:','Artist - ')
                                        lyric = lyric.replace('al:','Album - ')
                                        removeString = "[1234567890.:]"
                                        for char in removeString:
                                            lyric = lyric.replace(char,'')
                                        aditmadzs.sendMessage(msg.to, str(lyric))
                            except Exception as error:
                                pass                                        
        
                        elif cmd.startswith("img food: "):
                           if  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          #if msg._from in admin:
                                query = msg.text.replace("img food: ","")
                                r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/" + query + "?offset=1")
                                data=r.text
                                data=json.loads(r.text)
                                if data != []:
                                    for food in data:
                                        aditmadzs.sendImageWithURL(msg.to, str(food["url"]))
                                        
                        elif cmd.startswith("profilesmule: "):
                           if  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          #if msg._from in admin:    
                            try:
                                separate = msg.text.split(" ")
                                smule = msg.text.replace(separate[0] + " ","")
                                links = ("https://smule.com/"+smule)
                                ss = ("http://api2.ntcorp.us/screenshot/shot?url={}".format(urllib.parse.quote(links)))
                                aditmadzs.sendMessage(msg.to, "Sedang Mencari...")
                                time.sleep(2)
                                aditmadzs.sendMessage(msg.to, "ID Smule : "+smule+"\nLink : "+links)
                                aditmadzs.sendImageWithURL(msg.to, ss)
                            except Exception as error:
                                pass                                
                            	
                            	
                        elif cmd.startswith("meme"):
                           if  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          #if msg._from in admin:    
                            txt = msg.text.split("@")
                            image = ("http://memegen.link/"+txt[1].replace(" ","_")+"/"+txt[2].replace(" ","_")+"/"+txt[3].replace(" ","_")+".jpg?watermark=none")
                            aditmadzs.sendImageWithURL(msg.to, image)
          

                        elif cmd.startswith("ytmp4: "):
                           if  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          #if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']: 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n❧ Author : ' + str(vid.author)
                                    durasi = '\n❧ Duration : ' + str(vid.duration)
                                    suka = '\n❧ Likes : ' + str(vid.likes)
                                    rating = '\n❧ Rating : ' + str(vid.rating)
                                    deskripsi = '\n❧ Deskripsi : ' + str(vid.description)
                                aditmadzs.sendVideoWithURL(msg.to, me)
                                aditmadzs.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                aditmadzs.sendMessage(msg.to,str(e))

                        elif cmd.startswith("ytmp3: "):
                           if  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          #if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                bestaudio = vid.getbestaudio()
                                bestaudio.bitrate
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    shi = bestaudio.url
                                    me = best.url
                                    vin = s.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n❧ Author : ' + str(vid.author)
                                    durasi = '\n❧ Duration : ' + str(vid.duration)
                                    suka = '\n❧ Likes : ' + str(vid.likes)
                                    rating = '\n❧ Rating : ' + str(vid.rating)
                                    deskripsi = '\n❧ Deskripsi : ' + str(vid.description)
                                aditmadzs.sendImageWithURL(msg.to, me)
                                aditmadzs.sendAudioWithURL(msg.to, shi)
                                aditmadzs.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                aditmadzs.sendMessage(msg.to,str(e))
                                    
                        elif cmd.startswith("profileig: "):
                           if  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          #if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                html = requests.get('https://www.instagram.com/' + instagram + '/?')
                                soup = BeautifulSoup(html.text, 'html.parser')
                                data = soup.find_all('meta', attrs={'property':'og:description'})
                                text = data[0].get('content').split()
                                data1 = soup.find_all('meta', attrs={'property':'og:image'})
                                text1 = data1[0].get('content').split()
                                AR = text1[0].replace("s150x150/","")
                                user = "Name: " + text[-2] + "\n"
                                user1 = "Username: " + text[-1] + "\n"
                                followers = "Followers: " + text[0] + "\n"
                                following = "Following: " + text[2] + "\n"
                                post = "Post: " + text[4] + "\n"
                                link = "Link: " + "https://www.instagram.com/" + instagram
                                detail = "========INSTAGRAM INFO ========\n"
                                details = "\n========INSTAGRAM INFO ========"
                                aditmadzs.sendMessage(msg.to, detail + user + user1 + followers + following + post + link + details)
                                aditmadzs.sendImageWithURL(msg.to, AR)
                            except Exception as njer:
                                aditmadzs.sendMessage(msg.to, str(njer))
                                
                        elif cmd.startswith("cekig:"):
                           if  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                            #if msg._from in admin:
                                try:
                                    sep = text.split(" ")
                                    search = text.replace(sep[0] + " ","")
                                    r = requests.get("https://farzain.xyz/api/ig_profile.php?apikey=arTdnVbJkW1EuzDNQrIxQDvHARIDcQ&id={}".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data != []:
                                        ret_ = "┏━━[ Profile Instagram ]"
                                        ret_ += "\n┃┃ Nama : {}".format(str(data["info"]["full_name"]))
                                        ret_ += "\n┃┃ Username : {}".format(str(data["info"]["username"]))
                                        ret_ += "\n┃┃ Bio : {}".format(str(data["info"]["bio"]))
                                        ret_ += "\n┃┃ URL Bio : {}".format(str(data["info"]["url_bio"]))
                                        ret_ += "\n┃┃ Pengikut : {}".format(str(data["count"]["followers"]))
                                        ret_ += "\n┃┃ Diikuti : {}".format(str(data["count"]["followers"]))
                                        ret_ += "\n┃┃ Total Post : {}".format(str(data["count"]["post"]))
                                        ret_ += "\n┗━━[ https://www.instagram.com/{} ]".format(search)
                                        path = data["info"]["profile_pict"]
                                        aditmadzs.sendMessage(to, str(ret_))
                                        aditmadzs.sendImageWithURL(to, str(path))
                                except Exception as e:
                                    aditmadzs.sendMessage(msg.to, str(e))                                  

                        elif cmd.startswith("cekdate: "):
                           if  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          #if msg._from in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91A6Rs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            aditmadzs.sendMessage(msg.to,"🐚 I N F O R M A S I 🐚\n\n"+"🐚 Date Of Birth : "+lahir+"\n🐚 Age : "+usia+"\n🐚 Ultah : "+ultah+"\n🐚 Zodiak : "+zodiak)

                        elif cmd.startswith("แทค: "):
                           if  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                             if wait["selfbot"] == True:
                           #if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["ADITMADZSlimit"] = num
                                aditmadzs.sendMessage(msg.to,"Total Spamtag Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamcall: "):
                           if  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                             if wait["selfbot"] == True:
                           #if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                aditmadzs.sendMessage(msg.to,"Total Spamcall Diubah Menjadi " +strnum)

                        elif cmd.startswith("แทค "):
                           if  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                             if wait["selfbot"] == True:
                           #if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["ADITMADZSlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                aditmadzs.sendMessage1(msg)
                                            except Exception as e:
                                                aditmadzs.sendMessage(msg.to,str(e))
                                    else:
                                        aditmadzs.sendMessage(msg.to,"Jumlah melebihi 1000")
                                        
                        elif cmd == "spamcall" and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          if wait["selfbot"] == True:
                           #if msg._from in admin:
                             if msg.toType == 2:
                                group = aditmadzs.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                aditmadzs.sendMessage(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        aditmadzs.sendMessage(msg.to,str(e))
                                else:
                                    aditmadzs.sendMessage(msg.to,"Jumlah melebihi batas")

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           #if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      aditmadzs.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '5'}, contentType=9)
                                      ki.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           #if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      aditmadzs.sendMessage(midd, str(Setmain["ADITMADZSmessage1"]))
                                      ki.sendMessage(midd, str(Setmain["ADITMADZSmessage1"]))

                                  
                        elif 'Mybottoken' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in creator:
                               aditmadzs.sendMessage(msg.to,"Aditmadzs\n"+aditmadzs.authToken)
                               aditmadzs.sendMessage(msg.to,"KI\n"+ki.authToken)


#===========Settings============#
                                                           

                        elif 'ต้อนรับ ' in msg.text:
                           #if msg._from in admin:
                              spl = msg.text.replace('ต้อนรับ ','')
                              if spl == 'on' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    aditmadzs.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                                    
#===========Protection============#                                    

                        elif 'กันลิ้ง ' in msg.text:
                           #if msg._from in admin:
                              spl = msg.text.replace('กันลิ้ง ','')
                              if spl == 'on' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                                  if msg.to in protectqr:
                                       msgs ="ป้องกันลิ้งกลุ่ม โอเค"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "ป้องกันลิ้ง\nกลุ่ม : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "ป้องกันลิ้ง\nกลุ่ม : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url sudah tidak aktif"
                                    aditmadzs.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'กันเตะ ' in msg.text:
                           #if msg._from in admin:
                              spl = msg.text.replace('กันเตะ ','')
                              if spl == 'on' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                                  if msg.to in protectkick:
                                       msgs = "ป้องกันลบสมาชิก เรียบร้อย"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "เปิดป้องกันลบสมาชิก\nกลุ่ม : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "ป้องกันลบสมาชิก\nกลุ่ม : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    aditmadzs.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'กันเข้า ' in msg.text:
                           #if msg._from in admin:
                              spl = msg.text.replace('กันเข้า ','')
                              if spl == 'on' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                                  if msg.to in protectjoin:
                                       msgs = "Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Protect join diaktifkan\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Protect join dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    aditmadzs.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'กันยก ' in msg.text:
                           #if msg._from in admin:
                              spl = msg.text.replace('กันยก ','')
                              if spl == 'on' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Protect cancel diaktifkan\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Protect cancel dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    aditmadzs.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                                    
                        elif 'กันเชิญ ' in msg.text:
                           #if msg._from in admin:
                              spl = msg.text.replace('กันเชิญ ','')
                              if spl == 'on' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                                  if msg.to in protectinvite:
                                       msgs = "Protect invite sudah aktif"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Protect invite diaktifkan\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Protect invite dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect invite sudah tidak aktif"
                                    aditmadzs.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)                                                                      

                        elif 'กันหมด ' in msg.text:
                           #if msg._from in admin:
                              spl = msg.text.replace('กันหมด ','')
                              if spl == 'on' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectinvite:
                                      msgs = ""
                                  else:
                                      protectinvite.append(msg.to)                                      
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = aditmadzs.getGroup(msg.to)
                                      msgs = "เปิดป้องกันทั้งหมด\nกลุ่ม : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = aditmadzs.getGroup(msg.to)
                                      msgs = "เปิดป้องกันทั้งหมด\nกลุ่ม: " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                    else:
                                         msgs = ""                                         
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Berhasil menonaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                    else:
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Semua protect sudah off\nDi Group : " +str(ginfo.name)
                                    aditmadzs.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

#===========KICKOUT============#

                        elif ("Kick1 " in msg.text):
                            if sender in ["ue8d4c133178ae5a305354ddc71b1e577"]:
                              if wait["selfbot"] == True:
                            #if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

#===========ADMIN ADD============#
                        elif ("เพิ่มแอดมิน " in msg.text):
                            if sender in ["ue8d4c133178ae5a305354ddc71b1e577"]:
                              if wait["selfbot"] == True:
                           # if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin[target] = True
                                           f=codecs.open('admin.json','w','utf-8')
                                           json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)                                            
                                           aditmadzs.sendMessage(msg.to,"เพิ่มแอดมิน เรียบร้อย")
                                       except:
                                           pass

                        elif ("Staffadd " in msg.text):
                            if sender in ["ue8d4c133178ae5a305354ddc71b1e577"]:
                              if wait["selfbot"] == True:
                            #if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           aditmadzs.sendMessage(msg.to,"เพิ่มสต๊าฟ เรียบร้อย")
                                       except:
                                           pass

                        elif ("เพิ่มบอท " in msg.text):
                          if sender in ["ue8d4c133178ae5a305354ddc71b1e577"]:
                              if wait["selfbot"] == True:
                            #if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           aditmadzs.sendMessage(msg.to,"เพิ่มบอท เรียบร้อย")
                                       except:
                                           pass

                        elif ("ลบแอดมิน " in msg.text):
                            if sender in ["ue8d4c133178ae5a305354ddc71b1e577"]:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del admin[target]
                                           f=codecs.open('admin.json','w','utf-8')
                                           json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)                                            
                                           aditmadzs.sendMessage(msg.to,"ลบ เรียบร้อย")
                                       except:
                                           pass

                        elif ("ลบสต๊าฟ " in msg.text):
                            #if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Aditmadzs:
                                       try:
                                           staff.remove(target)
                                           aditmadzs.sendMessage(msg.to,"ลบ เรียบร้อย")
                                       except:
                                           pass

                        elif ("ลบบอท " in msg.text):
                            #if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Aditmadzs:
                                       try:
                                           Bots.remove(target)
                                           aditmadzs.sendMessage(msg.to,"ลบ เรียบร้อย")
                                       except:
                                           pass

                        elif cmd == "admin:on" or text.lower() == 'admin:on' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                            #if msg._from in admin:
                                wait["addadmin"] = True
                                aditmadzs.sendMessage(msg.to,"เรียบร้อย")

                        elif cmd == "admin:delete" or text.lower() == 'admin:delete' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                            #if msg._from in admin:
                                wait["delladmin"] = True
                                aditmadzs.sendMessage(msg.to,"เรียบร้อย")

                        elif cmd == "staff:on" or text.lower() == 'staff:on' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                            #if msg._from in admin:
                                wait["addstaff"] = True
                                aditmadzs.sendMessage(msg.to,"เรียบร้อย")

                        elif cmd == "staff:delete" or text.lower() == 'staff:delete' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                            #if msg._from in admin:
                                wait["dellstaff"] = True
                                aditmadzs.sendMessage(msg.to,"เรียบร้อย")

                        elif cmd == "bot:on" or text.lower() == 'bot:on' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                            #if msg._from in admin:
                                wait["addbots"] = True
                                aditmadzs.sendMessage(msg.to,"เรียบร้อย")

                        elif cmd == "bot:delete" or text.lower() == 'bot:delete' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                            #if msg._from in admin:
                                wait["dellbots"] = True
                                aditmadzs.sendMessage(msg.to,"เรียบร้อย")

                        elif cmd == "refresh" or text.lower() == 'refresh' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                            #if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                aditmadzs.sendMessage(msg.to,"Berhasil di Refresh...")

                        elif cmd == "contact admin" or text.lower() == 'contact admin' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                                ma = ""
                                for i in admin:
                                    ma = ki.getContact(i)
                                    ki.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact staff" or text.lower() == 'contact staff' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                                ma = ""
                                for i in staff:
                                    ma = ki.getContact(i)
                                    ki.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact bot" or text.lower() == 'contact bot' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                                ma = ""
                                for i in Bots:
                                    ma = ki.getContact(i)
                                    ki.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "notag on" or text.lower() == 'notag on' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                wait["Mentionkick"] = True
                                aditmadzs.sendMessage(msg.to,"Notag diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag off' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                wait["Mentionkick"] = False
                                aditmadzs.sendMessage(msg.to,"Notag dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                wait["contact"] = True
                                aditmadzs.sendMessage(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                wait["contact"] = False
                                aditmadzs.sendMessage(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "respon on" or text.lower() == 'respon on' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                wait["detectMention"] = True
                                aditmadzs.sendMessage(msg.to,"Auto respon diaktifkan")

                        elif cmd == "respon off" or text.lower() == 'respon off' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                wait["detectMention"] = False
                                aditmadzs.sendMessage(msg.to,"Auto respon dinonaktifkan")
                                
                        elif cmd == "respongift on" or text.lower() == 'respongift on' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                wait["Mentiongift"] = True
                                aditmadzs.sendMessage(msg.to,"Auto respon gift diaktifkan")

                        elif cmd == "respongift off" or text.lower() == 'respongift off' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                wait["Mentiongift"] = False
                                aditmadzs.sendMessage(msg.to,"Auto respon gift dinonaktifkan")                                

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                wait["autoJoin"] = True
                                aditmadzs.sendMessage(msg.to,"ok")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                wait["autoJoin"] = False
                                aditmadzs.sendMessage(msg.to,"ok")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                wait["autoLeave"] = True
                                aditmadzs.sendMessage(msg.to,"Auto Leave Diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                wait["autoLeave"] = False
                                aditmadzs.sendMessage(msg.to,"Auto Leave Dimatikan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                wait["autoAdd"] = True
                                aditmadzs.sendMessage(msg.to,"Auto Add Diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                wait["autoAdd"] = False
                                aditmadzs.sendMessage(msg.to,"Auto Add Dimatikan")

                        elif cmd == "sticker on" or text.lower() == 'sticker on' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                wait["sticker"] = True
                                aditmadzs.sendMessage(msg.to,"Detect Sticker Diaktifkan")

                        elif cmd == "sticker off" or text.lower() == 'sticker off' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                wait["sticker"] = False
                                aditmadzs.sendMessage(msg.to,"Detect Sticker Dimatikan")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                settings["autoJoinTicket"] = True
                                aditmadzs.sendMessage(msg.to,"Auto Join Ticket Diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                settings["autoJoinTicket"] = False
                                aditmadzs.sendMessage(msg.to,"Auto ok")

#===========COMMAND BLACKLIST============#
                        elif ("Talkban " in msg.text):
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           aditmadzs.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Untalkban " in msg.text):
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           aditmadzs.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                aditmadzs.sendMessage(msg.to,"เรียบร้อย")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                aditmadzs.sendMessage(msg.to,"เรียบร้อย")

                        elif ("แบน " in msg.text):
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           aditmadzs.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           aditmadzs.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                wait["wblacklist"] = True
                                aditmadzs.sendMessage(msg.to,"เรียบร้อย")

                        elif cmd == "unban:on" or text.lower() == 'unban:on' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                wait["dblacklist"] = True
                                aditmadzs.sendMessage(msg.to,"เรียบร้อย")

                        elif cmd == "banlist" or text.lower() == 'banlist' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                              if wait["blacklist"] == {}:
                                aditmadzs.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +aditmadzs.getContact(m_id).displayName + "\n"
                                aditmadzs.sendMessage(msg.to,"⏩ Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                aditmadzs.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +aditmadzs.getContact(m_id).displayName + "\n"
                                aditmadzs.sendMessage(msg.to,"⏩ Talkban User\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    aditmadzs.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = aditmadzs.getContact(i)
                                        aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']: i}, contentType=13)

                        elif cmd == "เคลียแบน" or text.lower() == 'clearban' and  sender in ['ue8d4c133178ae5a305354ddc71b1e577']:
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = aditmadzs.getContacts(wait["blacklist"])
                              mc = "���%i」User Blacklist" % len(ragets)
                              aditmadzs.sendMessage(msg.to,"Sukses membersihkan " +mc)
#===========COMMAND SET============#
                        elif 'Set pesan: ' in msg.text:
                           #if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "Gagal mengganti Pesan Message")
                              else:
                                  wait["message"] = spl
                                  aditmadzs.sendMessage(msg.to, "「Pesan Msg」\nPesan Message diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'ข้อความต้อนรับ: ' in msg.text:
                           #if msg._from in admin:
                              spl = msg.text.replace('ข้อความต้อนรับ: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, " Welcome Message ok")
                              else:
                                  wait["welcome"] = spl
                                  aditmadzs.sendMessage(msg.to, "「Welcome Msg」\nWelcome Message diganti jadi :\n\n「{}」".format(str(spl)))
                                  
                        elif 'Set leave: ' in msg.text:
                           #if msg._from in admin:
                              spl = msg.text.replace('Set leave: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "Gagal mengganti Leave Message")
                              else:
                                  wait["leave"] = spl
                                  aditmadzs.sendMessage(msg.to, "「Leave Msg」\nLeave Message diganti jadi :\n\n「{}」".format(str(spl)))                                    

                        elif 'Set respon: ' in msg.text:
                           #if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "Gagal mengganti Respon Message")
                              else:
                                  wait["Respontag"] = spl
                                  aditmadzs.sendMessage(msg.to, "「Respon Msg」\nRespon Message diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           #if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["ADITMADZSmessage1"] = spl
                                  aditmadzs.sendMessage(msg.to, "「Spam Msg」\nSpam Message diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'อ่าน: ' in msg.text:
                           #if msg._from in admin:
                              spl = msg.text.replace('อ่าน: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "ตั้งข้อความอ่านแล้ว")
                              else:
                                  wait["mention"] = spl
                                  aditmadzs.sendMessage(msg.to, "「Sider Msg」\n :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            #if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "「Pesan Msg」\nPesan Message lu :\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "cek welcome":
                            #if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "「Welcome Msg」\nWelcome Message lu :\n\n「 " + str(wait["welcome"]) + " 」")
                               
                        elif text.lower() == "cek leave":
                            #if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "「Leave Msg」\nLeave Message lu :\n\n「 " + str(wait["leave"]) + " 」")                                 

                        elif text.lower() == "cek respon":
                            #if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "「Respon Msg」\nRespon Message lu :\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cek spam":
                            #if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "「Spam Msg」\nSpam Message lu :\n\n「 " + str(Setmain["ADITMADZSmessage1"]) + " 」")

                        elif text.lower() == "cek sider":
                            #if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "「Sider Msg」\nSider Message lu :\n\n「 " + str(wait["mention"]) + " 」")

#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = aditmadzs.findGroupByTicket(ticket_id)
                                     aditmadzs.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     aditmadzs.sendMessage(msg.to, "AditmadzsOTW MASUK KE GROUP : %s" % str(group.name))
                                     group1 = ki.findGroupByTicket(ticket_id)
                                     ki.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     ki.sendMessage(msg.to, "Aditmadzs OTW MASUK KE GROUP : %s" % str(group.name))


    except Exception as error:
        print (error)


while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
               # bot(op)
                # Don't remove this line, if you wan't get error soon!
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                #thread1.daemon = True
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
