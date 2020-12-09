import json
from datetime import datetime
import os
import shutil

you = input("Enter Your Instagram name: ")
class Chat:
    global you, dpath
    def __init__(self, chat):
        self.data = chat #contains one chat in dictionary form
        self.participants = None
        self.conversation = None
        self.you = you
        self.other = None

    def extract_info(self):
        self.participants = self.data['participants']
        self.conversation = self.data['conversation']

        if self.participants[0] == self.you:
            self.other = self.participants[1]
        else:
            self.other = self.participants[0]

    def changeDate(self, main):
        for i in main:
            x = i['created_at']
            t = x[11:19]
            x = x[0:10]
            i['created_at'] = x
            i['time'] = t

        return main

    def format_conversation(self):
        self.extract_info()
        main = []
        l = len(self.conversation) - 1
        for i in range(l,-1,-1):
            main.append(self.conversation[i]) #sorting from frist chat to last chat

        main = self.changeDate(main)

        ################################## Getting total Unique dates##########################
        dates = []
        for i in main:
            dates.append(i['created_at'])

        dup_date = set(dates)
        dates = list(dup_date)
        dates.sort(key=lambda date: datetime.strptime(date, '%Y-%m-%d'))
        #########################################################################################

        fileName = self.other + '.txt'
        filePath = os.path.join(dpath, fileName)
        f = open(filePath, 'a', encoding='utf8')
        temp = main.copy()
        cd = 0
        flag = True
        while len(temp) != 0:
            if temp[0]['created_at'] == dates[cd]:
                x = temp[0]
                if flag == True:
                    #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", x['created_at'],"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    s = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + str(x['created_at']) + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
                    f.write(s)
                    #print()
                    flag = False

                if x['sender'] == self.you:
                    f.write("\n")
                    try:
                        if 'story_share' in x.keys():
                            space = " "*50
                           # print(space, "---",x['story_share'], "<", x['time'], ">", "\n")
                            s = space + "---" + x['story_share'] + "<" + x['time'] + ">" + '\n'
                            f.write(s)
                    except:
                        pass

                    try:
                        space = " " * 50
                       # print(space, "---", x['text'], "<", x['time'], ">")
                        s = space + "---" + x['text'] + "<" + x['time'] + ">" + '\n'
                        f.write(s)
                    except:
                        space = " " * 50
                       # print(space, "---", "!!!There is a media file!!!", "<", x['time'], ">")
                        s = space + "---" + "!!!There is a media file!!!" + "<" + x['time'] + ">" + '\n'
                        f.write(s)

                    f.write("\n")
                else:
                    f.write("\n")
                    try:
                        if 'story_share' in x.keys():
                           # print(x['story_share'],"<", x['time'], ">","\n")
                            s = x['story_share'] + "<" + x['time'] + ">" + '\n'
                            f.write(s)
                    except:
                        pass

                    try:
                       # print(x['text'], "<", x['time'], ">")
                        s = x['text'] + "<" + x['time'] + ">" + '\n'
                        f.write(s)
                    except:
                       # print("!!!There is a media file!!!", "<", x['time'], ">")
                        s = "!!!There is a media file!!!" + "<" + x['time'] + ">" + '\n'
                        f.write(s)

                    f.write("\n")
                temp.pop(0)
            else:
                flag = True
                cd += 1


        f.close()

class GroupChat(Chat):
    global grp_dpath

    def __init__(self, chat, num=-1):
        super(GroupChat, self).__init__(chat)
        self.num = num


    def extract_info(self):
        self.participants = self.data['participants']
        self.conversation = self.data['conversation']

    def format_conversation(self):
        self.extract_info()
        main = []
        l = len(self.conversation) - 1
        for i in range(l, -1, -1):
            main.append(self.conversation[i])  # sorting from frist chat to last chat

        main = self.changeDate(main)

        ################################## Getting total Unique dates##########################
        dates = []
        for i in main:
            dates.append(i['created_at'])

        dup_date = set(dates)
        dates = list(dup_date)
        dates.sort(key=lambda date: datetime.strptime(date, '%Y-%m-%d'))
        #########################################################################################

        try:
            os.mkdir(grp_dpath)
        except:
            pass

        fileName = "Grp_chat"+ str(self.num) + '.txt'
        filePath = os.path.join(grp_dpath, fileName)
        f = open(filePath, 'a', encoding='utf8')
        temp = main.copy()
        cd = 0
        flag = True
        while len(temp) != 0:
            if temp[0]['created_at'] == dates[cd]:
                x = temp[0]
                if flag == True:
                    #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", x['created_at'],"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    s = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + str(x['created_at']) + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
                    f.write(s)
                    #print()
                    flag = False

                if x['sender'] == self.you:
                   # print()
                    f.write("\n")
                    try:
                        if 'story_share' in x.keys():
                            space = " " * 50
                            #print(space, "---", x['story_share'], "<", x['time'], ">", "\n")
                            s = space + "---" + x['story_share'] + "<" + x['time'] + ">" + '\n'
                            f.write(s)
                    except:
                        pass

                    try:
                        space = " " * 50
                        #print(space, "---", x['text'], "<", x['time'], ">")
                        s = space + "---" + x['text'] + "<" + x['time'] + ">" + '\n'
                        f.write(s)
                    except:
                        space = " " * 50
                       # print(space, "---", "!!!There is a media file!!!", "<", x['time'], ">")
                        s = space + "---" + "!!!There is a media file!!!" + "<" + x['time'] + ">" + '\n'
                        f.write(s)

                   # print()
                    f.write("\n")
                else:
                    #print()
                    f.write("\n")
                   # print(">>>[ ", x['sender'], " ]")
                    s = ">>>[ " + x['sender'] + " ]" + "\n"
                    f.write(s)
                    try:
                        if 'story_share' in x.keys():
                            #print(x['story_share'], "<", x['time'], ">", "\n")
                            s = x['story_share'] + "<" + x['time'] + ">" + '\n'
                            f.write(s)
                    except:
                        pass

                    try:
                        #print(x['text'], "<", x['time'], ">")
                        s = x['text'] + "<" + x['time'] + ">" + '\n'
                        f.write(s)
                    except:
                        #print("!!!There is a media file!!!", "<", x['time'], ">")
                        s = "!!!There is a media file!!!" + "<" + x['time'] + ">" + '\n'
                        f.write(s)

                temp.pop(0)
            else:
                flag = True
                cd += 1

                #print()
                f.write("\n")

        f.close()


##############################################################

dpath = r'C:\Users\91982\Desktop\chats'
grp_dpath = r'C:\Users\91982\Desktop\chats\grp_chats'
try:
    shutil.rmtree(dpath, ignore_errors=True)
    os.mkdir(dpath)
except:
    pass

path = 'messages.json'
with open(path, encoding='utf8') as f:
    data = json.load(f)


for num,d in enumerate(data):
    if len(d['participants']) == 2:
        chat = Chat(d)
        chat.format_conversation()
    else:
        chat = GroupChat(d,num)
        chat.format_conversation()

print("Done")
