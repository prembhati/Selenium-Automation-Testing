
FROM python:3.9-slim
WORKDIR /app
COPY . /app
COPY C:\\Windows\\chromedriver.exe /usr/local/bin/chromedriver
RUN pip install selenium
CMD ["python", "instagram_automation.py"]
