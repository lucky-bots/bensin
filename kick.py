#!/usr/bin/python3
# -*- coding: utf-8 -*- 

import LINEPY
from LINEPY import *
from akad.ttypes import *
#from linedynamicflex import *
from __MACOSX import *
from thrift.unverting import *
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
from googletrans import Translator
import youtube_dl

bot1 = LineClient("caceca5085@simdpi.com","Aa1234")
#bot1 = LineClient(authToken='token')
bot1.log("Auth Token : " + str(bot1.authToken))
channel = LineChannel(bot1)
bot1.log("Channel Access Token : " + str(channel.channelAccessToken))

bot2 = LineClient("fefegi4817@jesdoit.com","Aa1234")
#ki = LineClient(authToken='Token')
bot2.log("Auth Token : " + str(bot2.authToken))
channel1 = LineChannel(bot2)
bot2.log("Channel Access Token : " + str(channel1.channelAccessToken))

#ubah mid di dalem admin,owner,bensin.json dengan mid kalian

with open('bensin.json', 'r') as c:
    datac = json.load(c)
with open('owner.json', 'r') as o:
    datao = json.load(o)
with open('admin.json', 'r') as a:
    dataa = json.load(a)
with open('api.json', 'r') as ap:
    api = json.load(ap)
    
datas = 'ue8d4c133178ae5a305354ddc71b1e577'    
poll = LinePoll(bot1)
call = bot1
bensin = datac
owner = datao
admin = dataa
staff = datas
mid = bot1.getProfile().mid
Amid = bot2.getProfile().mid
KAC = [bot1,bot2]
ABC = [bot2,bot1,datas,dataa,datao,datac]
Bots = [mid,Amid]
All = [datas,dataa,datao,datac,bot1,bot2]
rfu = [bot1]


print ("success")

api = {"kw":{}}
protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []

welcome = []
simisimi = []
translateen = []
translateid = []
translateth = []
translatetw = []
translatear = []



myProfile = {
    "displayName": "",
    "statusMessage": "",
    "pictureStatus": ""
}

bot1Profile = bot1.getProfile()
myProfile["displayName"] = bot1Profile.displayName
myProfile["statusMessage"] = bot1Profile.statusMessage
myProfile["pictureStatus"] = bot1Profile.pictureStatus

responsename1 = bot2.getProfile().displayName

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

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
        f = codecs.open('api.json','w','utf-8')
        json.dump(api, f, sort_keys=True, indent=4, ensure_ascii=False)
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
        textx = "สมาชิกทั้งหมด {}\n  [ Mention ]\n1. ".format(str(len(mid)))
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
                    no = "\n┗━━[ {} ]".format(str(bot1.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        bot1.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        bot1.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "=> ".format(str(len(mid)))
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
                    no = "\n┗━━[ {} ]".format(str(bot1.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        bot1.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        bot1.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "ยินดีต้อนรับสมาชิกใหม่\n =>  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = bot1.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nกลุ่ม "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(bot1.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        bot1.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        bot1.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "มีสมาชิกออกกลุ่ม\nบายย  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = bot1.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["leave"]+"\nกลุ่ม "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(bot1.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        bot1.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        bot1.sendMessage(to, "[ INFO ] Error :\n" + str(error))        

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = bot1.getAllContactIds()
        gid = bot1.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"◐ Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\n🐚 Group : "+str(len(gid))+"\n🐚 Teman : "+str(len(teman))+"\n🐚 Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n🐚 Runtime : \n • "+bot
        bot1.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        bot1.sendMessage(to, "[ INFO ] Error :\n" + str(error))

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
    helpMessage = """╭───────────
➻ บอท => @เบนซิน ➻
╰───────────
╭─────────────
│〖 Menu => ADMIN 〗
├─────────────
├➻ คำสั่ง〖〗
├➻ คำสั่ง2〖〗
├➻ คำสั่งowner
├➻ คำสั่งบันชี
├➻ สปีด
├➻ รีบอท
├➻ ข้อมูล〖〗
├➻ เพิ่มสต๊าฟ
╰─────────────
 
╭─────────────
│〖 เลฃบันชีเพื่อน 〗
├─────────────
├➻  เบน  
├➻  ปุ้น
├➻  ฟอร์ด
├➻  บอย
├➻  บำ
├➻  น้อง
├➻ 
╰─────────────
"""
    return helpMessage
    
    

def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = """╭─────────────
➻ บอท   =>   @เบนซิน ➻
╰─────────────
╭─────────────
│วิธีใช้ => คำสั่ง => ทั้งหมด  
├─────────────
├➻ 〖
├➻ 〖
├➻ 〖
├➻ 〖
├➻ 〖
├➻ 
├➻ 
├➻ 〖
├➻ 
╰─────────────
"""
    return helpMessage1
    
def infomeme():
    helpMessage2 = """╭────────────
➻ บอท => @เบนซิน ➻
╰──────────────
╭─────────────
│〖 หมวดแทคทั้งหมด 〗
├─────────────
├➻ แทค〖แท้อง〗
├➻ แทค〖ตาข〗
├➻ คท @〖ด
├➻ ชื่อ @〖lllอ〗
├➻ ตัส @〖ดึl〗
├➻ mid @〖ดึ
├➻ รูป @〖ดึงล์〗
├➻ ปก @〖ดึ
├➻ วีดีโอ @ดีโอ〗
├➻ บันทึก〖
├➻ ก็อป @〖ก〗
├➻ กลับร่าง〖〗
├➻ สแปมแทค〖〗
├➻ ตั้งสแปมแทค〖〗
╰─────────────
"""
    return helpMessage2
    
def translate():
    helpTranslate =  """╭──────────
➻ บอท => @เบนซิน ➻
╰──────────────
╭──────────────
│〖 คำสั่งและลูกเล่นอื่น 〗
├──────────────
├➻ 
├➻ อ่าน〖ดูคนแอบอ่าน〗
├➻ เชคapi〖〗
├➻ ตั้งapi้〗
├➻ ล้างapi〖〗
├➻ เขียน〖ข้อความ〗
├➻ ไอดีไลน์〖〗
╰──────────────
"""
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
                    if bot1.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            bot1.reissueGroupTicket(op.param1)
                            X = bot1.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            bot1.updateGroup(X)
                            bot1.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    try:
                        if bot2.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                bot2.reissueGroupTicket(op.param1)
                                X = bot2.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                bot2.updateGroup(X)
                                bot1.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                    except:
                        pass
                                                
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        bot1.acceptGroupInvitation(op.param1)
                        ginfo = bot1.getGroup(op.param1)
                        bot1.sendMessage(op.param1,"วัน\n กลุ่ม " +str(ginfo.name))
                        bot1.leaveGroup(op.param1)
                    else:
                        bot1.acceptGroupInvitation(op.param1)
                        ginfo = bot1.getGroup(op.param1)
                        bot1.sendMessage(op.param1,"=> " + str(ginfo.name))

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        bot1.acceptGroupInvitation(op.param1)
                        ginfo = bot1.getGroup(op.param1)
                        bot1.sendMessage(op.param1,"สวัสดีครับ, บอทมาแล้วครับ ^^")
                    else:
                        bot1.acceptGroupInvitation(op.param1)
                        ginfo = bot1.getGroup(op.param1)
                        bot1.sendMessage(op.param1,"สวัสดีครับ, บอทมาแล้วครับ^^")
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        bot2.acceptGroupInvitation(op.param1)
                        ginfo = bot2.getGroup(op.param1)
                        bot2.sendMessage(op.param1,"ลาก่อน\n กลุ่ม " +str(ginfo.name))
                        bot2.leaveGroup(op.param1)
                    else:
                        bot2.acceptGroupInvitation(op.param1)
                        ginfo = bot2.getGroup(op.param1)
                        bot2.sendMessage(op.param1,"ดี " + str(ginfo.name))

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = bot1.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            random.choice(KAC).cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = bot2.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                random.choice(KAC).cancelGroupInvitation(op.param1,[_mid])
                        except:
                            pass

        if op.type == 15:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = bot1.getGroup(op.param1)
                contact = bot1.getContact(op.param2).picturePath
                image = 'http://dl.profile.bot1.naver.jp'+contact
                leaveMembers(op.param1, [op.param2])
                bot1.sendImageWithURL(op.param1, image)

       

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = bot1.getGroup(op.param1)
                contact = bot1.getContact(op.param2)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                welcomeMembers(op.param1, [op.param2])
                bot1.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            bot2.kickoutFromGroup(op.param1,[op.param2])
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
                        bot1.sendMessage(op.param1, wait["message"])
       
        
        
        
        
        
        
        
        
        
        
#===========KICK============#
        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass  
#==================================

        if op.type == 32:
            if op.param1 in protectcancel:
              if op.param3 in Bots:    
                if op.param2 not in Bots and op.param2 not in All:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            bot2.findAndAddContactsByMid(op.param1,[Zmid])
                            bot2.kickoutFromGroup(op.param1,[op.param2])
                            bot2.inviteIntoGroup(op.param1,[Zmid])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                bot1.findAndAddContactsByMid(op.param1,[Zmid])
                                bot1.kickoutFromGroup(op.param1,[op.param2])
                                bot1.inviteIntoGroup(op.param1,[Zmid])
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
                        bot2.inviteIntoGroup(op.param1,[op.param3])
                        bot1.acceptGroupInvitation(op.param1)
                        bot2.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            G = bot2.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            bot2.updateGroup(G)
                            Ticket = bot2.reissueGroupTicket(op.param1)
                            bot1.acceptGroupInvitationByTicket(op.param1,Ticket)
                            bot2.kickoutFromGroup(op.param1,[op.param2])
                            G = bot2.getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            bot2.updateGroup(G)
                            Ticket = bot2.reissueGroupTicket(op.param1)
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
                        bot1.inviteIntoGroup(op.param1,[op.param3])
                        bot2.acceptGroupInvitation(op.param1)
                        bot1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            G = bot1.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            bot1.updateGroup(G)
                            Ticket = bot1.reissueGroupTicket(op.param1)
                            bot2.acceptGroupInvitationByTicket(op.param1,Ticket)
                            bot1.kickoutFromGroup(op.param1,[op.param2])
                            G = bot1.getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            bot1.updateGroup(G)
                            Ticket = bot1.reissueGroupTicket(op.param1)
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
                        bot2.findAndAddContactsByMid(op.param1,admin)
                        bot2.inviteIntoGroup(op.param1,admin)
                        bot2.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            bot1.findAndAddContactsByMid(op.param1,admin)
                            bot1.inviteIntoGroup(op.param1,admin)
                            bot1.kickoutFromGroup(op.param1,[op.param2])
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
                        bot2.findAndAddContactsByMid(op.param1,staff)
                        bot2.inviteIntoGroup(op.param1,staff)
                        bot2.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            bot1.findAndAddContactsByMid(op.param1,staff)
                            bot1.inviteIntoGroup(op.param1,staff)
                            bot1.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass

                return

        if op.type == 55:
            try:
                if op.param1 in Setmain["bot1readPoint"]:
                   if op.param2 in Setmain["bot1readMember"][op.param1]:
                       pass
                   else:
                       Setmain["bot1readMember"][op.param1][op.param2] = True
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
                    Name = bot1.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = bot1.getContact(op.param2)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
              #          bot1.sendImageWithURL(op.param1, image)                        
                        
                    
        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = bot1.getGroup(at)
                                bot1.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Gambar Dihapus 」\n• ผู้ส่ง : "
                                ret_ = "• ชื่อกลุ่ม : {}".format(str(ginfo.name))
                                ret_ += "\n• เวลาส่ง : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(bot1.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':bot1.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                bot1.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                bot1.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = bot1.getGroup(at)
                                bot1.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 Pesan Dihapus 」\n"
                                ret_ += "• ผู้ส่ง : {}".format(str(bot1.displayName))
                                ret_ += "\n• ชื่อกลุ่ม: {}".format(str(ginfo.name))
                                ret_ += "\n• เวลาส่ง : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n• ข้อความ : {}".format(str(msg_dict[msg_id]["text"]))
                                bot1.sendMessage(at, str(ret_))
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
                                ginfo = bot1.getGroup(at)
                                bot1.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "「 Sticker Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(bot1.displayName))
                                ret_ += "\n• ชื่อกลุ่ม: {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                bot1.sendMessage(at, str(ret_))
                                bot1.sendImage(at, msg_dict1[msg_id]["data"])
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
                    path = bot1.downloadObjectMsg(msg_id)
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
                            path = bot1.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
                                                      
                            
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    bot1.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nไอดี : " + msg.contentMetadata["STKPKGID"] + "\nเวอร์ชั่น : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    bot1.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = bot1.getContact(msg.contentMetadata["mid"])
                        path = bot1.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.bot1.naver.jp'+path
                        bot1.sendMessage(msg.to,"⏩ Nama : " + msg.contentMetadata["displayName"] + "\n⏩ MID : " + msg.contentMetadata["mid"] + "\n⏩ Status : " + contact.statusMessage + "\n⏩ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        bot1.sendImageWithURL(msg.to, image)
#===========ADD BOT============#
               if msg.contentType == 13:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        bot1.sendMessage(msg.to,"ผู้ติดต่อเป็นสมาชิกบอทอยู่แล้ว")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        bot1.sendMessage(msg.to,"เพิ่มสมาชิกบอทสำเร็จแล้ว")
                        
                  if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        bot1.sendMessage(msg.to,"")
                    else:
                        wait["dellbots"] = True
                        bot1.sendMessage(msg.to,"ผู้ติดต่อไม่ใช่สมาชิกของ BEN BOT")
#===========ADD STAFF=========
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        bot1.sendMessage(msg.to,"ผู้ติดต่อเป็นพนักงานอยู่แล้ว")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        bot1.sendMessage(msg.to,"เพิ่มพนักงานเรียบร้อยแล้ว")
                  if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        bot1.sendMessage(msg.to,"ลบ สต๊าฟแล้ว")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        bot1.sendMessage(msg.to,"ไม่มีข้อมูลนี้")
#===========ADD ADMIN============#
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        bot1.sendMessage(msg.to,"ไม่มีข้อมูลนี้")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        bot1.sendMessage(msg.to,"เพิ่มแอดมินสำเร็จ")
                  if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        bot1.sendMessage(msg.to, "ลบแอดมินสำเร็จ")
                    else:
                        wait["delladmin"] = True
                        bot1.sendMessage(msg.to,"")
#========ADD BLACKLIST=========#
            
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        bot1.sendMessage(msg.to,"มีข้อมูลในแบ็คลิส")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        bot1.sendMessage(msg.to,"เพิ่มลงในแบล็คลิสแล้ว")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        bot1.sendMessage(msg.to,"นำออกจากบัญชีดำใช้สำเร็จแล้ว")
                    else:
                        wait["dblacklist"] = True
                        bot1.sendMessage(msg.to,"ผู้ติดต่อไม่อยู่ในบัญชีดำ")
#===========TALKBAN============
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        bot1.sendMessage(msg.to,"ผู้ติดต่ออยู่ใน Talkban อยู่แล้ว")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        bot1.sendMessage(msg.to,"เพิ่มไปยังผู้ใช้ Talkban เรียบร้อยแล้ว")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        bot1.sendMessage(msg.to,"ลบออกจากผู้ใช้ Talkban สำเร็จ")
                    else:
                        wait["Talkdblacklist"] = True
                        bot1.sendMessage(msg.to,"ผู้ติดต่อไม่อยู่ใน Talkban")
#===========UPDATE FOTO============#
               if msg.contentType == 1:
                  if  Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line -apps.com/talk/m/download.nhn?oid="+msgid
                        headers = bot1.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            bot1.sendMessage(msg.to, "success")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                  if settings["groupPicture"] == True:
                     path = bot1.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     bot1.updateGroupPicture(msg.to, path)
                     bot1.sendMessage(msg.to, "success")

               if msg.contentType == 1:
                  if mid in Setmain["bot1foto"]:
                            path = bot1.downloadObjectMsg(msg_id)
                            del Setmain["bot1foto"][mid]
                            bot1.updateProfilePicture(path)
                            bot1.sendMessage(msg.to,"ok")

               if msg.contentType == 1:
                  if Amid in Setmain["bot1foto"]:
                            path = bot2.downloadObjectMsg(msg_id)
                            del Setmain["bot1foto"][Amid]
                            bot2.updateProfilePicture(path)
                            bot2.sendMessage(msg.to,"แก้ไขรูปภาพเรียบร้อยแล้ว")

               if msg.contentType == 1:
                  if settings["changePicture"] == True:
                     path1 = bot2.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     bot2.updateProfilePicture(path1)
                     bot2.sendMessage(msg.to, "bot ok")               

               if msg.contentType == 0:
                  if Setmain["autoRead"] == True:
                        bot1.sendChatChecked(msg.to, msg_id)
                        
               if text is None:
                        return
               else:
                        cmd = command(text)
               if op.type == 26 or op.type == 25:
                  msg = op.message
                  sender = msg._from
                  try:
                      if api["kw"][str(msg.text)]:
                         bot1.sendMessage(msg.to,api["kw"][str(msg.text)])
                  except:
                      pass
 #========= START CODE ==========# 
               if msg.text.lower() == "api":
                    mas = "╭────────────"
                    mas += "\n│ดูตัวอย่าง:\n│ตั้งapi เทส;;เทสอะไรครับ"
                    mas += "\n│ต้องมี ;; ทุกครั้ง"
                    mas += "\n╰────────────"
                    bot1.sendMessage(msg.to,mas)
               if msg.text.lower() == "เชคapi":
                    lisk = "[ คำสั่งตอบโต้ ]\n"
                    for i in api["kw"]:
                        lisk+="\nคีย์เวิร์ด: "+str(i)+"\nตอบโต้: "+str(api["kw"][i])+"\n"
                    bot1.sendMessage(msg.to,lisk)
               if msg.text.startswith("ล้างapi "):
                    try:
                        delcmd = msg.text.split(" ")
                        getx = msg.text.replace(delcmd[0] + " ","")
                        del api["kw"][getx]
                        bot1.sendMessage(msg.to, "คำตอบโต้ " + str(getx) + " ล้างแล้ว")
                        f=codecs.open('api.json','w','utf-8')
                        json.dump(api, f, sort_keys=True, indent=4, ensure_ascii=False)
                    except Exception as Error:
                        print(Error)
               if msg.text.startswith("ตั้งapi "):
                    try:
                        delcmd = msg.text.split(" ")
                        get = msg.text.replace(delcmd[0]+" ","").split(";;")
                        kw = get[0]
                        ans = get[1]
                        api["kw"][kw] = ans
                        f=codecs.open('api.json','w','utf-8')
                        json.dump(api, f, sort_keys=True, indent=4, ensure_ascii=False)
                        bot1.sendMessage(msg.to,"คีย์เวิร์ด: " + str(kw) + "\nตอบกลับ: " +str(ans))
                    except Exception as Error:
                        print(Error)
               if cmd == "คำสั่ง" and sender in All:
                   if wait["selfbot"] == True:
                       helpMessage = help()
                       bot1.sendMessage(msg.to, str(helpMessage))
               if cmd == "testbug":
                  if sender in  All:
                       bot1.sendMessage(msg.to, "ไลน์ไม่บัคครับ")
                  else: 
                        bot2.sendMessage(msg.to, sender)
                        tme.sleep(1)
                        bot1.sendMessage(msg.to, "ไลน์คุนบัค เอาข้อความ bot2 ติดต่อ เบนซิน")
               if cmd == "bss":
                  if sender in bensin:
                     if wait["selfbot"] == True:
                        helpMessage1 = helpbot()
                        bot1.sendMessage(msg.to, str(helpMessage1))
                  else: 
                        bot1.sendMessage(msg.to, "คุนไม่มีสิทธิ์สั่ง")
               if cmd == "คำสั่ง2":
                  if sender in All:
                     if wait["selfbot"] == True:
                          helpMessage2 = infomeme()
                          bot1.sendMessage(msg.to, str(helpMessage2))
                  else: 
                        bot1.sendMessage(msg.to, "คุนไม่มีสิทธิ์สั่ง")   
               
               if cmd == "ผู้สร้าง" or text.lower() == 'ผู้สร้าง':
                  if sender in All:
                       bot1.sendMessage(msg.to,"คนทำบอท") 
                       ma = ""
                  for i in bensin:
                       ma = bot1.getContact(i)
                       bot1.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
                  else: 
                        bot1.sendMessage(msg.to, "คุนไม่มีสิทธิ์สั่ง")         
               
               if cmd == "about" or cmd == "ข้อมูล" and sender in All:
                  if wait["selfbot"] == True:
              
                     try:
                        arr = []
                        x = bot1.getContact(owner)
                        contact = bot1.getContact(lineMID)
                        grouplist = bot1.getGroupIdsJoined()
                        contactlist = bot1.getAllContactIds()
                        blockedlist = bot1.getBlockedContactIds()
                        IdsInvit = bot1.getGroupIdsInvited()
                        times = time.time() - lineStart
                        runtime = timeChange(times)
                        ret_ = "╭───「 About Your 」"
                        ret_ += "\n├ ชื่อ : {}".format(contact.displayName)
                        ret_ += "\n├ กลุ่ม : {}".format(str(len(grouplist)))
                        ret_ += "\n├ เพื่อน : {}".format(str(len(contactlist)))
                        ret_ += "\n├ บล็อค : {}".format(str(len(blockedlist)))
                        ret_ += "\n├ ค้างเชิญ : {}".format(str(len(IdsInvit)))
                        ret_ += "\n├────────────"
                        ret_ += "\n├ เวลาออนบอท :"
                        ret_ += "\n├ {}".format(str(runtime))
                        ret_ += "\n├────────────"
                        ret_ += "\n├ ผู้สร้าง : {}".format(str(bensin.displayName))
                        ret_ += "\n╰───「 About Your 」"
                        bot1.sendMessage(msg.to, str(ret_))
                        bot1.sendContact(msg.to, bensin.mid)
                     except Exception as e:
                        bot1.sendMessage(msg.to, str(e))

               
               if cmd == "ฉัน" or text.lower() == 'ฉัน':
                  if sender in All:
                     if wait["selfbot"] == True:
                        msg.contentType = 13
                        
                        msg.contentMetadata = {'mid': msg._from}
                        bot1.sendMessage1(msg)

                  else: 
                        bot1.sendMessage(msg.to, "คุนไม่มีสิทธิ์สั่ง")
               
               if text.lower() == "มิดฉัน":
                  if sender in All:
                               bot1.sendMessage(msg.to, msg._from)

                  else: 
                        bot1.sendMessage(msg.to, "คุนไม่มีสิทธิ์สั่ง")
               
               if ("มิด " in msg.text):
                  if sender in All:
                     if wait["selfbot"] == True:
                        key = eval(msg.contentMetadata["MENTION"])
                        key1 = key["MENTIONEES"][0]["M"]
                        mi = bot1.getContact(key1)
                        bot1.sendMessage(msg.to, "sender : "+str(mi.displayName)+"\nMID : " +key1)
                        bot1.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                                 
                  else: 
                        bot1.sendMessage(msg.to, "คุนไม่มีสิทธิ์สั่ง")

               if cmd == "บอท":
                  if sender in All:
                     if wait["selfbot"] == True:
                        msg.contentType = 13
                        msg.contentMetadata = {'mid': mid}
                        bot1.sendMessage1(msg)
                        msg.contentType = 13
                        msg.contentMetadata = {'mid': Amid}
                        bot1.sendMessage1(msg)
                  else:
                       bot1.sendMessage(msg.to, "คุนไม่มีสิทธิ์สั่ง")

               if text.lower() == "ลบแชท":
                  if sender in All:
                     if wait["selfbot"] == True:
                        try:
                           bot1.removeAllMessages(op.param2)
                        except:
                             pass
                               
                  else: 
                      bot1.sendMessage(msg.to, "คุนไม่มีสิทธิ์สั่ง")
               
               if text.lower() == "ลบ":
                  if sender in All:
                     if wait["selfbot"] == True:
                        try:
                          bot2.removeAllMessages(op.param2)
                          bot1.sendMessage(msg.to,"success.")
                        except:
                             pass
                  else: 
                     bot1.sendMessage(msg.to, "คุนไม่มีสิทธิ์สั่ง")
               
               if cmd.startswith("ben: "):
                  if sender in All:
                     if wait["selfbot"] == True:
                        sep = text.split(" ")
                        pesan = text.replace(sep[0] + " ","")
                        saya = bot1.getGroupIdsJoined()
                        for group in saya:
                            bot1.sendMessage(group,"=====[ B E N ]====\n"+pesan+"\n รับติดตั้งบอท")

                  else: 
                        bot1.sendMessage(msg.to, "คุนไม่มีสิทธิ์สั่ง")
               
               if text.lower() == "mykey":
                  if sender in All:
                     if wait["selfbot"] == True:
                        bot1.sendMessage(msg.to, "「Mykey」\nSetkey bot mu「 " + str(Setmain["keyCommand"]) + " 」")
                               
                  else: 
                      bot1.sendMessage(msg.to, "คุนไม่มีสิทธิ์สั่ง")
               
               if cmd.startswith("setkey "):
                  if sender in All:
                     if wait["selfbot"] == True:
                        sep = text.split(" ")
                        key = text.replace(sep[0] + " ","")
                        if key in [""," ","\n",None]:
                           bot1.sendMessage(msg.to, "Gagal mengganti key")
                        else: Setmain["keyCommand"] = str(key).lower()
                        bot1.sendMessage(msg.to, "「Setkey」\nSetkey diganti jadi「{}」".format(str(key).lower()))

                  else: 
                      bot1.sendMessage(msg.to, "คุนไม่มีสิทธิ์สั่ง")
               
               if text.lower() == "resetkey":
                  if sender in All:
                     if wait["selfbot"] == True: Setmain["keyCommand"] = ""
                     bot1.sendMessage(msg.to, "「Setkey」\nSetkey mu kembali ke awal")

                  else: 
                        bot1.sendMessage(msg.to, "คุนไม่มีสิทธิ์สั่ง")
               
               if cmd == "รีสตาร์ท":
                  if sender in bensin:
                     if wait["selfbot"] == True:
                      bot1.sendMessage(msg.to, "รีสตาร์ทบอทแล้ว")
                      Setmain["restartPoint"] = msg.to
                      restartBot()
                            
                  else: 
                        bot1.sendMessage(msg.to, "คุนไม่มีสิทธิ์สั่ง")
               
               if cmd == "บอทรัน":
                  if sender in All:
                     if wait["selfbot"] == True:
                        eltime = time.time() - mulai
                        bot = "Aktif " +waktu(eltime)
                        bot1.sendMessage(msg.to,bot)
                            
                  else: 
                        bot1.sendMessage(msg.to, "คุนไม่มีสิทธิ์สั่ง")
               elif cmd == "เปิดลิ้ง":
                   if sender in All:
                       if wait["selfbot"] == True:
                           if msg.toType == 2:
                                   X = bot2.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   bot2.updateGroup(X)
                                   bot2.sendMessage(msg.to, "เปิดลิ้งกลุ่มเรียบร้อย")

                   else: 
                        bot1.sendMessage(msg.to, "คุนไม่มีสิทธิ์สั่ง")
               
               elif cmd == "ปิดลิ้ง":
                   if sender in All:
                       if wait["selfbot"] == True:
                           if msg.toType == 2:
                                   X = bot2.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   bot2.updateGroup(X)
                                   bot2.sendMessage(msg.to, "ปิดลิ้งกลุ่มเรียบร้อย")

                   else: 
                        bot1.sendMessage(msg.to, "คุนไม่มีสิทธิ์สั่ง")
               
               elif cmd == "ลิ้ง":
                   if sender in All:
                       if wait["selfbot"] == True:
                           if msg.toType == 2:
                              x = bot2.getGroup(msg.to)
                              if x.preventedJoinByTicket == True:
                                 x.preventedJoinByTicket = False
                                 bot2.updateGroup(x)
                                 gurl = bot2.reissueGroupTicket(msg.to)
                                 bot2.sendMessage(msg.to, "ชื่อ : "+str(x.name)+ "\nUrl grup : http://bot1.me/R/ti/g/"+gurl)
                   else: 
                        bot1.sendMessage(msg.to, "คุนไม่มีสิทธิ์สั่ง")
               
               elif cmd == "reject":
                   if sender in All:
                       if wait["selfbot"] == True:
                           ginvited = bot1.getGroupIdsInvited()
                           if ginvited != [] and ginvited != None:
                               for gid in ginvited:
                                   bot1.rejectGroupInvitation(gid)
                                   abot1.sendMessage(to, "Berhasil tolak sebanyak {} undangan grup".format(str(len(ginvited))))
                   else:
                       bot1.sendMessage(to, "ไม่มีคำเชิญที่รอดำเนินการ")
               
               elif cmd == "เปลี่ยนรูปกลุ่ม":
                   if sender in All:
                       if wait["selfbot"] == True:
                           if msg.toType == 2:
                               settings["groupPicture"] = True
                               bot1.sendMessage(msg.to,"ส่งรูปมา")   
                   else:
                       bot1.sendMessage(msg.to, "คุนไม่มีสิทธิ์สั่ง")
               
               elif cmd == "เปลี่ยนรูปบอท":
                   if sender in All:
                       if wait["selfbot"] == True:
                           settings["changePicture"] = True
                           bot2.sendMessage(msg.to,"ส่งรูปมา....")
                                
                   else: 
                        bot1.sendMessage(msg.to, "คุนไม่มีสิทธิ์สั่ง")
               
               elif cmd == "เปลี่ยนรูปบอท1":
                   if sender in All:
                       if wait["selfbot"] == True:
                           Setmain["bot1foto"][mid] = True
                       bot1.sendMessage(msg.to,"ส่งรูปมา....")
                                
                   else: 
                        bot1.sendMessage(msg.to, "คุนไม่มีสิทธิ์สั่ง")
               
               elif cmd == "อัพบอท1":
                   if sender in All:
                       Setmain["bot1foto"][Amid] = True
                       bot2.sendMessage(msg.to,"ส่งรูปมา....")
                               

                   else: 
                        bot1.sendMessage(msg.to, "คุนไม่มีสิทธิ์สั่ง")
               
               elif cmd.startswith("ชื่อ: "):
                   if sender in All:
                       separate = msg.text.split(" ")
                       string = msg.text.replace(separate[0] + " ","")
                       if len(string) <= 10000000000:
                           profile = bot1.getProfile()
                           profile.displayName = string
                           bot1.updateProfile(profile)
                           bot1.sendMessage(msg.to,"เปลี่ยนชื่อเป็น =>" + string + "เรียบร้อยจ้า")

                   else: 
                        bot1.sendMessage(msg.to, "คุนไม่มีสิทธิ์สั่ง")
               
               elif cmd.startswith("ชื่อบอท: "):
                   if sender in All:
                       separate = msg.text.split(" ")
                       string = msg.text.replace(separate[0] + " ","")
                       if len(string) <= 10000000000:
                           profile = bot2.getProfile()
                           profile.displayName = string
                           bot2.updateProfile(profile)
                           bot2.sendMessage(msg.to,"เปลี่ยนชื่อเป็น " + string + "เรียบร้อย")

#===========BOT UPDATE============#
                   else: 
                        bot1.sendMessage(msg.to, "คุนไม่มีสิทธิ์สั่ง")
               
               elif cmd == "แทค" or text.lower() == '😆':
                   if sender in All:
                       if wait["selfbot"] == True:
                           group = bot1.getGroup(msg.to)
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
               
               elif cmd == "ลิสบอท":
                          if wait["selfbot"] == True:
                            if sender in All:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +bot1.getContact(m_id).displayName + "\n"
                                bot1.sendMessage(msg.to,"⏩ BOT\n\n"+ma+"\nรวม「%s บอทT" %(str(len(Bots))))
               
               elif cmd == "ลิสแอดมิน":
                          if wait["selfbot"] == True:
                            if sender in All:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +bot1.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +bot1.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +bot1.getContact(m_id).displayName + "\n"
                                bot1.sendMessage(msg.to,"BEN\n\nผู้สร้าง:\n"+ma+"\nแอดมิน:\n"+mb+"\nสต๊าฟ:\n"+mc+"\nรวม %s」" %(str(len(owner)+len(admin)+len(staff))))
               elif cmd == "/บอท":
                   if sender in All:
                       if wait["selfbot"] == True:
                           try:
                                    anggota = [Amid]
                                    bot1.inviteIntoGroup(msg.to, anggota)
                                    bot2.acceptGroupInvitation(msg.to)
                           except:
                                pass
                   else: 
                        bot1.sendMessage(msg.to, "คุนไม่มีสิทธิ์สั่ง")
               
               elif cmd == "/บอท1":
                   if sender in All:
                       if wait["selfbot"] == True:
                           G = bot1.getGroup(msg.to)
                           ginfo = bot1.getGroup(msg.to)
                           G.preventedJoinByTicket = False
                           bot1.updateGroup(G)
                           invsend = 0
                           Ticket = bot1.reissueGroupTicket(msg.to)
                           bot2.acceptGroupInvitationByTicket(msg.to,Ticket)
                           G = gg.getGroup(msg.to)
                           G.preventedJoinByTicket = True
                           bot2.updateGroup(G)

                   else: 
                        bot1.sendMessage(msg.to, "คุนไม่มีสิทธิ์สั่ง")
               
               elif cmd == "/ไป":
                   if sender in All:
                       if wait["selfbot"] == True:
                           G = bot1.getGroup(msg.to)
                           bot2.sendMessage(msg.to, "ลาก่อน กลุ่ม  "+str(G.name))
                           bot2.leaveGroup(msg.to)
                   else:
                       bot1.sendMessage(msg.to, "คุนไม่มีสิทธิ์สั่ง")
               
               elif cmd.startswith("leave "):
                   if sender in All:
                       proses = text.split(" ")
                       ng = text.replace(proses[0] + " ","")
                       gid = bot1.getGroupIdsJoined()
                       for i in gid:
                           h = bot1.getGroup(i).name
                           if h == ng:
                               bot2.sendMessage(i, "Silahkan admin invite atau masukan kembali")
                               bot2.leaveGroup(i)
                               bot1.sendMessage(to,"Berhasil keluar dari grup " +h)
                   else: 
                        bot1.sendMessage(msg.to, "คุนไม่มีสิทธิ์สั่ง")
               
               elif cmd == "/มา":
                   if sender in All:
                       G = bot1.getGroup(msg.to)
                       ginfo = bot1.getGroup(msg.to)
                       G.preventedJoinByTicket = False
                       bot1.updateGroup(G)
                       invsend = 0
                       Ticket = bot1.reissueGroupTicket(msg.to)
                       bot2.acceptGroupInvitationByTicket(msg.to,Ticket)
                       
                       G = bot2.getGroup(msg.to)
                       G.preventedJoinByTicket = True
                       bot2.updateGroup(G)
                   else: 
                       bot1.sendMessage(msg.to, "คุนไม่มีสิทธิ์สั่ง")
               
               elif cmd == "เทส":
                   if sender in All:
                          if wait["selfbot"] == True:
                              get_profile_time_start = time.time()
                              get_profile = bot1.getProfile()
                              get_profile_time = time.time() - get_profile_time_start
                              get_group_time_start = time.time()
                              get_group = bot1.getGroupIdsJoined()
                              get_group_time = time.time() - get_group_time_start
                              get_contact_time_start = time.time()
                              get_contact = bot1.getContact(mid)
                              get_contact_time = time.time() - get_contact_time_start
                              bot1.sendMessage(msg.to, "ความเร็วตอบกลับ\n\n - ดึงโปรไฟล์\n   %.10f\n - ดึงคอนแทค\n   %.10f\n - ตอบกลับกลุ่ม\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))
               
               elif cmd == "สปีด" or cmd == "sp" in Msg.text:
                          if wait["selfbot"] == True:
                            if sender in All:
                               start = time.time()
                               bot1.sendMessage(msg.to, "สปีด....")
                               elapsed_time = time.time() - start
                               bot1.sendMessage(msg.to, "{} วินาที".format(str(elapsed_time)))
                            else: bot1.sendMessage(msg.to, sender)
               
               elif cmd == "อ่าน":
                          if wait["selfbot"] == True:
                           if sender in All:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  bot1.sendMessage(msg.to, "ระบบจับสมาชิกอ่าน\nวัน : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nเวลา  [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True
                           else: bot1.sendMessage(msg.to, sender)
               
               elif cmd == "ปิดอ่าน":
                          if wait["selfbot"] == True:
                           if sender in All:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  bot1.sendMessage(msg.to, "ปิดจับอ่าน \nวัน : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nเวลา [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  bot1.sendMessage(msg.to, "Sudak tidak aktif")

#===========Hiburan============#
               
               elif cmd.startswith("profilesmule: "):
                          if sender in All:    
                            try:
                                separate = msg.text.split(" ")
                                smule = msg.text.replace(separate[0] + " ","")
                                links = ("https://smule.com/"+smule)
                                ss = ("http://api2.ntcorp.us/screenshot/shot?url={}".format(urllib.parse.quote(links)))
                                bot1.sendMessage(msg.to, "Sedang Mencari...")
                                time.sleep(2)
                                bot1.sendMessage(msg.to, "ID Smule : "+smule+"\nLink : "+links)
                                bot1.sendImageWithURL(msg.to, ss)
                            except Exception as error:
                                pass
               
               elif cmd.startswith("meme"):
                          if sender in All:    
                            txt = msg.text.split("@")
                            image = ("http://memegen.link/"+txt[1].replace(" ","_")+"/"+txt[2].replace(" ","_")+"/"+txt[3].replace(" ","_")+".jpg?watermark=none")
                            bot1.sendImageWithURL(msg.to, image)
          
               elif cmd.startswith("แทค: "):
                          if wait["selfbot"] == True:
                           if sender in All:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["bot1limit"] = num
                                bot1.sendMessage(msg.to,"ตั้งแทคเรียบร้อย " +strnum)

               
               elif cmd.startswith("แทค "):
                          if wait["selfbot"] == True:
                           if sender in All:
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
                                    jmlh = int(Setmain["bot1limit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                bot1.sendMessage1(msg)
                                            except Exception as e:
                                                bot1.sendMessage(msg.to,str(e))
                                    else:
                                        bot1.sendMessage(msg.to,"Jumlah melebihi 1000")
                                  
               
               elif 'โทเค็น' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in bensin:
                               bot1.sendMessage(msg.to,"bot1\n"+bot1.authToken)
                               bot1.sendMessage(msg.to,"KI\n"+bot2.authToken)

#=================================
               
               elif cmd == 'ต้อนรับ ' in msg.text and sender in All:
                              ppl = msg.text.replace('ต้อนรับ ','')
                              if ppl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = bot1.getGroup(msg.to)
                                       msgs = "อ่านกฎกลุ่ม ด้วยนะครับ by แอดมิน\n กลุ่ม: " +str(ginfo.name)
                                  bot1.sendMessage(msg.to, "「Bot => Ben」\n" + msgs)
               
                              elif ppl == 'off':
                                  if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = bot1.getGroup(msg.to)
                                         msgs = "ปิด => ต้อนรับ \nกลุ่ม : " +str(ginfo.name)
                                  else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                         bot1.sendMessage(msg.to, "「Bot By Ben」\n" + msgs)
                                    
#===========Protection============#
               elif 'rm ' in msg.text and sender in All:
                   ppl = msg.text.replace('rm ',"")
                   response = requests.post('https://api.remove.bg/v1.0/removebg',
                   data={'image_url': ppl,
                   'size': 'auto'},
                   headers={'X-Api-Key': '7645PPax87Sc8DvwXjTeXvj6'},)
                   if response.status_code == requests.codes.ok:
                       with open('no-bg.png', 'wb') as out:
                           rmg = out.write(response.content)
                           bot2.sendMessage(msg.to,rmg)
                   else:
                       print("Error:", response.status_code, response.text)

                                
               elif 'กันหมด ' in msg.text and sender in All:
                              ppl = msg.text.replace('กันหมด ','')
                              if ppl == 'on':
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
                                      ginfo = bot1.getGroup(msg.to)
                                      msgs = "เปิดป้องกัน => ทั้งหมด \n กลุ่ม : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = bot1.getGroup(msg.to)
                                      msgs = "เปิดป้องกันทั้งหมด\n กลุ่ม : " +str(ginfo.name)
                                  bot1.sendMessage(msg.to, "「Bot => Ben」\n" + msgs)
            
               
                              elif ppl == 'off':
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
                                                      ginfo = bot1.getGroup(msg.to)
                                                      msgs = " ปิดป้องกัน => ทั้งหมด \n กลุ่ม : " +str(ginfo.name)
                                  else:
                                    ginfo = bot1.getGroup(msg.to)
                                    msgs = "ยังไม่ได้เปิดป้องกัน \n กลุ่ม : " +str(ginfo.name)
                                    bot1.sendMessage(msg.to, "「Bot => Ben」\n" + msgs)

#===========KICKOUT============#

               
               elif ("เตะ " in msg.text):
                          if wait["selfbot"] == True:
                            if sender in All:
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
                          if wait["selfbot"] == True:
                            if sender in bensin or sender in owner:
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
                                           bot1.sendMessage(msg.to,"เพิ่มแอดมินเรียบร้อย")
                                       except:
                                           pass
               
               
               elif ("เพิ่มสต๊าฟ " in msg.text):
                          if wait["selfbot"] == True:
                            if sender in All:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           bot1.sendMessage(msg.to,"เพิ่มสต๊าฟเรียบร้อย")
                                       except:
                                           pass


               
               elif ("เพิ่มบอท " in msg.text):
                          if wait["selfbot"] == True:
                            if sender in All:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           bot1.sendMessage(msg.to,"เพิ่มบอทเรียบร้อย")
                                       except:
                                           pass

               
               elif ("ลบแอดมิน " in msg.text):
                            if sender in bensin:
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
                                           bot1.sendMessage(msg.to,"ลบแอดมินเรียบร้อย")
                                       except:
                                           pass

            
               
               elif ("ลบสต๊าฟ " in msg.text):
                            if sender in All:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in bot1:
                                       try:
                                           staff.remove(target)
                                           bot1.sendMessage(msg.to,"ลบสต๊าฟเรียบร้อย")
                                       except:
                                           pass

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
                                     group = bot1.findGroupByTicket(ticket_id)
                                     bot1.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     bot1.sendMessage(msg.to, "bot1OTW MASUK KE GROUP : %s" % str(group.name))
                                     group1 = bot2.findGroupByTicket(ticket_id)
                                     bot2.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     bot2.sendMessage(msg.to, "bot1 OTW MASUK KE GROUP : %s" % str(group.name))
               
    

                
               
####################### new ########################

               
               
               
               
                     
 
 
 
 
 
 
 
 
 
 
 
  #========= END CODE ========#
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
