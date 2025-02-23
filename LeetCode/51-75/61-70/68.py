class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        i = 0
        flag = 1
        res = []
        while flag:
            res.append("")
            len_words = 0
            words_in_string = []
            # считаем сколько слов сможем уместить и сколько они будут занимать места
            while len_words + len(words[i]) <= maxWidth:
                len_words += len(words[i]) + 1 # + 1 тк рассчитываем место под пробелы
                words_in_string.append(words[i])
                i += 1
                if i == len(words):
                    flag = 0
                    break

            len_words -= len(words_in_string) #вычитаем пробелы, так как они могут быть не по одному, и нужен будет пересчет

            if len(words_in_string) == 1: #если длина 1, то все пробелы будут в конце
                kol_gaps = 1
            else:
                kol_gaps = len(words_in_string) - 1 #все пробелы между словами

            if not flag:
                    res[-1] = ' '.join(words_in_string) + ' ' * (maxWidth - len_words - len(words_in_string) + 1)
                    #если последняя строка, то все слова через 1 пробел, и в конце добавляем пробелы до необходимой длины
            else:
                ind = 0
                dif = maxWidth - len_words #сколько всего пробелов нужно будет вставить
                for word in words_in_string:
                    if dif != 0:
                        kol_space = dif // kol_gaps + 1 if dif % kol_gaps != 0 else dif // kol_gaps
                        #сколько сейчас нужно будет вставить пробелов
                        res[-1] += word + ' ' * kol_space
                        dif -= kol_space
                    else:
                        res[-1] += word
                    kol_gaps -= 1
        return res

instance = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
res = instance.fullJustify(words, maxWidth)

def print_res(res):
    for string in res:
       print(string, len(string))

print_res(res)

