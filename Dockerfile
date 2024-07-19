FROM python
WORKDIR /app
COPY . . 
COPY . /app/
CMD ["python", "Sharks E-Shop/main.py"]