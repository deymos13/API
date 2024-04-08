import requests



api_url = "https://randomuser.me/api/"
response = requests.get(api_url)   # Отправляем GET-запрос и сохраняем ответ в переменной response
if response.status_code == 200:    # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
    response_dict = response.json()
    result_data = response_dict["result"]
    dat1 = result_data["gender"]
    dat2 = result_data["name"]["first"]
    dat3 = result_data["name"]["last"]
    print("Гендер", dat1)
    print("Имя", dat2)
    print("Фамилия", dat3)
else:
    print(response.status_code)
