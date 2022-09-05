# coding:utf-8
import re

from .login_service import LoginService
from utils.exception_handler import exception_handler


class BlueCodeService(LoginService):
    """ 蓝码服务 """

    def __init__(self):
        super().__init__()
        self.pattern = re.compile(r"var text\s?=\s?'(.+)';")
        self.pass_code_url = "https://passcode.zju.edu.cn/pass_code/zx"

    @exception_handler('')
    def get_text(self):
        """ 获取通行码的数据 """
        if not self.login():
            return ''

        response = self.session.get(self.pass_code_url)
        match = self.pattern.search(response.text)
        return match.group(1) if match else ''
