import gettext

from language_system import LanguageSystem, language_mapping


# signup successfully
# reserve successfully
# cancel successfully

class Enus(LanguageSystem):
    def get_sentence(self, event_key: str):
        sentence: str = language_mapping["en-us"][event_key]  # event_key:對應事件key值
        return sentence  # # 返回對應事件英文

        # 建立翻譯物件
# trans = gettext.translation('myapp', localedir='locales', languages=['zh_TW'])
# trans.install()
#
# # 使用 gettext 函數 _() 來標記需要翻譯的字串
# print(_('Hello, world!'))
