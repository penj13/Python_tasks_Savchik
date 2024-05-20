search_words = ["watch new movies", "coffee near me", "how to find the determinant", "python", "data science jobs in UK", "courses for data science", "taxi", "google", "yandex", "bing", "foreign exchange rates USD/BYN", "Netflix movies watch online free",  "Statistics courses online from top universities"]


def percent_stats(count_words: str):
    list_of_searches = []
    dict_search_words = dict.fromkeys(count_words)
    
    for key, value in dict_search_words.items():
        spaces_key = key.split()
        value = len(spaces_key)
        list_of_searches.append(value)

    num_of_searches = len(list_of_searches)
    max_words_in_one_search = max(list_of_searches)
    
    for word_count in range(max_words_in_one_search+1):
        num_of_words = list_of_searches.count(word_count)
        percent_of_searches = num_of_words / num_of_searches
        if num_of_words > 0:
            if word_count % 10 in (2, 3, 4):
                i = "а"
            elif word_count % 10 in (0, 5, 6, 7, 8, 9):
                i = ""
            elif word_count % 10 in (1,):
                i = "о"
            print(f"{word_count} слов{i}: {percent_of_searches:.2%}")


percent_stats(search_words)


