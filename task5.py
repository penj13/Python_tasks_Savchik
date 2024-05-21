search_words = ["watch new movies", "coffee near me", "how to find the determinant", "python", "data science jobs in UK", "courses for data science", "taxi", "google", "yandex", "bing", "foreign exchange rates USD/BYN", "Netflix movies watch online free",  "Statistics courses online from top universities"]


def percent_stats(count_words: str):
#   формируем словарь из списка запросов
    dict_search = dict.fromkeys(count_words)
    num_of_searches = len(dict_search)
    num_of_values = []
    
#   формируем список количества слов каждого запроса
    for key, value in dict_search.items():
        spaces_key = key.split()
        value = len(spaces_key)
        num_of_values.append(value)

#   проверка
#   print(num_of_values)
#   print(max(num_of_values))

#   высчитываем процентное соотношение запросов с определенным количеством слов по отношению ко числу всех запросов и выводим на экран
    for word_count in range(1, max(num_of_values) + 1):
        num_of_words = num_of_values.count(word_count)
        percent_of_searches = num_of_words / num_of_searches
        if num_of_words > 0:
            if word_count % 10 in (2, 3, 4):
                i = "слова"
            elif word_count % 10 in (0, 5, 6, 7, 8, 9):
                i = "слов"
            elif word_count % 10 in (1,):
                i = "слово"
            print(f"{word_count} {i}: {percent_of_searches:.2%}")


percent_stats(search_words)
