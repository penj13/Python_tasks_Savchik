s = ["watch new movies", "coffee near me", "how to find the determinant", "python", "data science jobs in UK", "courses for data science", "taxi", "google", "yandex", "bing", "foreign exchange rates USD/BYN", "Netflix movies watch online free",  "Statistics courses online from top universities"]
def stat(s):
    n = len(s)
    n_1 = int(n)
    f = []
    i = 0
    for z in range(n_1):
        g = str(s[i])
        b = g.split()
        a = len(b)
        f.append(a)
        i += 1
    max_w = max(f)
    h = 1
    for z in range(max_w):
        pr = round(100*(f.count(h)/n_1), 2)
        if h%10 == 1:
            print(h,'слово:',pr,'%')
        elif h%10 == 2 or h%10 == 3 or h%10 == 4:
            print(h,'слова:',pr,'%')
        elif h%10 == 0 or h%10 == 5 or h%10 == 6 or h%10 == 7 or h%10 == 8 or h%10 == 9 or h == 11:
            print(h,'слов:',pr,'%')
        h += 1
stat(s)
