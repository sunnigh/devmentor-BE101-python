from abc import ABC, abstractmethod

# signup successfully
# reserve successfully
# cancel successfully
# 註冊成功
# 預約成功
# 取消成功
language_mapping = {
    "zh-tw": {
        "123": "註冊成功",
        "456": "預約成功",
        "789": "取消成功",
    },
    "en-us": {
        "123": "signup successfully",
        "456": "reserve successfully",
        "789": "cancel successfully",
    },
    "jp": {},
    "kr": {}
}


class LanguageSystem(ABC):

    @abstractmethod
    def get_sentence(self, event_key: str):
        pass
