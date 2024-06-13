# 使用官方的Python運行環境作為基礎映像檔
FROM python:3.8-slim-buster

# 建立app資料夾
Run mkdir /app

# 設定工作目錄
WORKDIR /app

# 將當前目錄的內容複製到容器的/app目錄
COPY . /app


# 當容器啟動時運行main.py
CMD ["python", "main.py"]
