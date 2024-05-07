import gettext

from language_system import LanguageSystem


class enus(LanguageSystem):
    def language(self):
        pass

        # 建立翻譯物件
trans = gettext.translation('myapp', localedir='locales', languages=['zh_TW'])
trans.install()

# 使用 gettext 函數 _() 來標記需要翻譯的字串
print(_('Hello, world!'))