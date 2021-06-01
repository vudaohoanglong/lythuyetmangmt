import os 
import socket 

class Process:
    def __init__(self,sk):
        self.sk=sk 
    def process_view(self):
        output = os.popen('powershell "gps |  select name, id, {$_.Threads.Count}').read()
        self.sk.sendall(bytes(str(len(output)),"utf8"))
        self.sk.sendall(bytes(output,"utf8"))
        pass
    def process_kill(self,sid):
        if not sid.isdigit():
            self.sk.sendall(bytes("fail","utf8"))
            return
        sid=int(sid)
        try:
            os.kill(sid,9)
        except OSError:
            self.sk.sendall(bytes("fail","utf8"))
            return
        self.sk.sendall(bytes("success","utf8"))
    def process_start(self, sid):
        if len(sid) == 0: return
        #pname += ".exe"
        try:
            os.popen(sid)
        except OSError:
            self.sk.send(bytes("fail", "utf8"))
            return
        self.sk.send(bytes("success", "utf8"))
        
