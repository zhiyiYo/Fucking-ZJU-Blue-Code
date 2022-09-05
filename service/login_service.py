# coding:utf-8
import json
import re

import requests
from utils.logger import logger


class LoginService:
    """ 浙大通行证登录服务 """

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }

        self.session = requests.session()
        self.login_url = "https://zjuam.zju.edu.cn/cas/login?service=http%3A%2F%2Fservice.zju.edu.cn%2F"

        with open("config/config.json", encoding="utf-8") as f:
            data = json.load(f)
            self.username = data["username"]
            self.password = data["password"]
            self.nickname = data.get("nickname") or self.username

    def login(self):
        """ 登录 """
        # 清空 Cookie
        self.session.cookies.clear()

        # 获取登录页面
        response = self.session.get(self.login_url)
        execution = re.search(
            'name="execution" value="(.*?)"', response.text).group(1)

        # 加密密码
        data = self.session.get(
            "https://zjuam.zju.edu.cn/cas/v2/getPubKey").json()
        m, e = data['modulus'], data['exponent']
        password = self._rsa_encrypt(self.password, e, m)

        # 登录
        data = {
            'username': self.username,
            'password': password,
            'execution': execution,
            '_eventId': 'submit',
            "authcode": ""
        }
        response = self.session.post(self.login_url, data)

        if '用户名或密码错误' in response.text:
            logger.error(self.nickname+"登录失败 😕")
            return False
        else:
            logger.info(self.nickname+"登陆成功 😊")
            return True

    def _rsa_encrypt(self, password, e, m):
        password = int.from_bytes(bytes(password, 'ascii'), 'big')
        result = pow(password, int(e, 16), int(m, 16))
        return hex(result)[2:].rjust(128, '0')