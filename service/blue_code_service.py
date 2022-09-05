# coding:utf-8
import re

from dataclasses import dataclass
from .login_service import LoginService
from utils.exception_handler import exception_handler


class BlueCodeService(LoginService):
    """ 蓝码服务 """

    def __init__(self):
        super().__init__()
        self.eduction_pattern = re.compile(
            r'<span class="bgr-blue">(.+)</span>')
        self.name_pattern = re.compile(r"<h3>(.{2,4})的通行码</h3>")
        self.code_pattern = re.compile(r"text:\s? '(.+)',")
        self.pass_code_url = "https://passcode.zju.edu.cn/pass_code/zx"

    @exception_handler('')
    def get_info(self):
        """ 获取通行码的数据 """
        if not self.login():
            return BlueCodeInfo()

        html = self.session.get(self.pass_code_url).text
        return BlueCodeInfo(
            self._match_text(self.name_pattern, html),
            self._match_text(self.eduction_pattern, html),
            self._match_text(self.code_pattern, html),
        )

    @staticmethod
    def _match_text(pattern: re.Pattern, text: str):
        """ match text """
        match = pattern.search(text)
        return match.group(1) if match else ''


@dataclass
class BlueCodeInfo:
    name: str = ''          # 学生姓名
    education: str = ''     # 本科生/研究生/博士生
    code: str = ''          # 二维码的数据
