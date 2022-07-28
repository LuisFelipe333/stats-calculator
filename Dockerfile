FROM python:3.9

COPY . /usr/src/app

WORKDIR /usr/src/app

#Instalamos dependencias
RUN python3 -m pip install -r requirements.txt


#Corremos
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]