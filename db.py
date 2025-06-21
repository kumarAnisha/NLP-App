import json
class database:
    def insert(self,name,email,password):
        with open('user.json' ,'r') as rf:
            data=json.load(rf)
            if email in data:
                return 0
            else:
                data[email]=[name,password]
        with open('user.json','w') as wf:
            json.dump(data,wf)
            return 1
    def search(self,email,password):
        with open('user.json','r') as rf:
         data=json.load(rf)
         if email not in data:
            return 0
         else:
            if data[email][1]==password:
                return 1
            else:
                return 0