from language_system import LanguageSystem, language_mapping


# 註冊成功
# 預約成功
# 取消成功

class Zhtw(LanguageSystem):
    def get_sentence(self, event_key: str):
        sentence: str = language_mapping["zh-tw"][event_key]  # event_key:對應事件key值
        return sentence  # 返回對應事件中文
