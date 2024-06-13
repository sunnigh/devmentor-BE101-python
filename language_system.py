from abc import ABC, abstractmethod

# signup successfully
# reserve successfully
# cancel successfully
# 註冊成功
# 預約成功
# 取消成功
language_mapping = {
    "zh-tw": {
        "signup": "註冊成功",
        "reserve": "預約成功",
        "cancel": "取消成功",
        "congratulate": "祝你新年快樂",
    },
    "en-us": {
        "signup": "signup successfully",
        "reserve": "reserve successfully",
        "cancel": "cancel successfully",
        "congratulate": "Happy Chinese New Year",
    },
    "jp": {},
    "kr": {}
}


# 所有語系一起放在language system內以便新增


class LanguageSystem(ABC):

    def get_sentence(self, event_key: str):
        sentence: str = language_mapping[self.get_language()][event_key]  # event_key:對應事件key值
        return sentence

    @abstractmethod
    def get_language(self):
        pass
