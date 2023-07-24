## Para rodar o sistema A
Requisitos Yolov5, Python, OpenCV e Pytorch:

para rodar a aplicação navegue a pasta pelo terminal, utilize o ambiente com YOLO e digite: 

`python programa.py`

para verificar o comando de exemplo de treinamento YOLO veja o arquivo

`comandoYOLO.txt`

## Para rodar o sistema B
Requisita docker, navegue pelo terminal WSL (se for Windows) até a pasta do docker e rode os comandos:

`sudo docker-compose run web python manage.py migrate`

`sudo docker-compose up --build`
