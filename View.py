from Controler import Event, Signup, Reserve, Cancel
from Model import LanSys


class User:
    """
    訪客選擇語系
    輸入username
    如果是user執行登入
    學生可以預約或取消課程
    """

    def __init__(self):
        self.student = Student()

    def displaymenu(self):
        username = input('請輸入用戶名:')
        print('輸入1選擇語系')
        print('輸入2顯示使用者當前身份')
        print('輸入3訪客執行登入')
        print('輸入4學生預約課程')
        print('輸入5學生取消課程')

    def select_num(self):
        num = input('請輸入欲執行動作編號:')
        if num == '1':
            self.select_lang()
        elif num == '2':
            self.displayidentity()
        elif num == '3':
            self.log_in()
        elif num == '4':
            self.student.reserve()
        elif num == '5':
            self.student.cancel()
        else:
            print('輸入錯誤')

    def select_lang(self):
        lang = input('請選擇語系:1.中文 2.English')
        #if lang == '1':

        pass

    def displayidentity(self):
        pass

    def login(self):

        pass

    def main(self):

        while True:  # 一直工作
            self.displaymenu()
            self.select_num()


class Student(User):
    """
        預約
        取消
    """

    def __init__(self):
        super().__init__()
        self.Reserve = Reserve()
        self.Cancel = Cancel()

    def reserve(self):
        self.Reserve.reserve()
        pass

    def cancel(self):
        self.Cancel.cancel()
        pass
