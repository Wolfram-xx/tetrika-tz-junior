import csv

import requests
from bs4 import BeautifulSoup

def search_page(url):


    # Получить содержимое страницы
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе страницы: {e}")
        exit()


    soup = BeautifulSoup(response.text, "html.parser")

    # Вытаскиваем все div-ы нужного класса (нам нужны все, кроме первых двух)
    target_divs = soup.find_all("div", class_="mw-category-group")
    return_list = {}
    last_elem = None
    for i in range(2, len(target_divs)):    # берем со третьего дива и до конца (тут каждый див это новая буква)
        li_elements = target_divs[i].find_all("li")

        last_elem = li_elements[len(li_elements) - 1].text.strip() # берем последний элемент, чтобы следующую страницу выводить с нее
        return_list[last_elem[0]] = len(li_elements)  # возвращаем длинну списка
    return return_list, last_elem


url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"

return_list, last_elem = search_page(url)
final_list = return_list
while 0 not in return_list.values():    # когда список закончится, вернет 0 элементов
    return_list, last_elem = search_page(f"https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom={last_elem}#mw-pages")
    return_list[list(return_list.keys())[0]] -= 1 # вычитаем 1, так как начинали с поледнего элемента прошлого списка
    for letter in return_list.keys():
        if letter in final_list:
            final_list[letter] += return_list[letter]
        else:
            final_list[letter] = return_list[letter]
    # print(return_list)
    # print(final_list)
    # print("-" * 20)
    # Красивый вывод


with open('beats.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for elem in final_list:
        writer.writerow([elem, final_list[elem]]) # Записываем в csv