from flask import Flask, request, Response
import requests

app = Flask(__name__)


# Функция для обработки запросов к зеркальному сайту
@app.route('/mirror', methods=['GET'])
def mirror():
    # Получаем URL исходного сайта из параметра запроса
    url = request.args.get('url')

    if not url:
        return Response('URL не указан', status=400)

    try:
        # Отправляем запрос к исходному сайту
        response = requests.get(url)

        # Возвращаем данные в ответ на запрос клиента
        return Response(response.content, status=response.status_code, content_type=response.headers['Content-Type'])
    except requests.RequestException as e:
        return Response('Ошибка при выполнении запроса: {}'.format(str(e)), status=500)


if __name__ == '__main__':
    app.run("0.0.0.0")
