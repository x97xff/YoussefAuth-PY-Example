"""
Youssef Auth - Official Python SDK v1.2
https://youssefauth.wuaze.com
"""

import hashlib
import json
import platform
import subprocess
import requests

class api:
    name = ""
    ownerid = ""
    secret = ""
    version = ""
    sessionid = ""
    encstatus = False
    base_url = "https://youssefauth.wuaze.com/api/1.2/"

    def __init__(self, name: str, ownerid: str, secret: str, version: str):
        self.name = name
        self.ownerid = ownerid
        self.secret = secret
        self.version = version

    def get_hwid(self) -> str:
        try:
            if platform.system() == "Windows":
                cmd = "wmic csproduct get uuid"
                return subprocess.check_output(cmd).decode().split('\n')[1].strip()
            return platform.node()
        except Exception:
            return "UNKNOWN_HWID"

    def init(self) -> bool:
        init_iv = hashlib.sha256(self.secret.encode()).hexdigest()[:16]
        data = {
            "type": "init",
            "ver": self.version,
            "hash": None,
            "enckey": init_iv,
            "name": self.name,
            "ownerid": self.ownerid
        }
        r = requests.post(self.base_url, data=data)
        try:
            res = r.json()
            if res.get("success"):
                self.sessionid = res.get("sessionid", "")
                self.encstatus = res.get("encstatus", False)
                return True
            else:
                print(f"[Youssef Auth] Init Error: {res.get('message', 'Unknown error')}")
                return False
        except Exception as e:
            print(f"[Youssef Auth] Network / JSON Error: {e}")
            return False

    def register(self, username, password, license_key):
        hwid = self.get_hwid()
        data = {
            "type": "register",
            "username": username,
            "pass": password,
            "key": license_key,
            "hwid": hwid,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }
        r = requests.post(self.base_url, data=data)
        return r.json()

    def login(self, username, password):
        hwid = self.get_hwid()
        data = {
            "type": "login",
            "username": username,
            "pass": password,
            "hwid": hwid,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }
        r = requests.post(self.base_url, data=data)
        return r.json()

    def license(self, license_key):
        hwid = self.get_hwid()
        data = {
            "type": "license",
            "key": license_key,
            "hwid": hwid,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }
        r = requests.post(self.base_url, data=data)
        return r.json()

    def var(self, varid):
        data = {
            "type": "var",
            "varid": varid,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }
        r = requests.post(self.base_url, data=data)
        return r.json()

    def log(self, message):
        data = {
            "type": "log",
            "message": message,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }
        requests.post(self.base_url, data=data)