class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        #когда есть пересечения код не работает, не знаю, можно ли решить задачу тем методом, которым я пошел
        #когда-нибудь стоит вернуться к данной задаче и перерешать ее или же доработать данный код

        dict_word = {}
        mass_flag = []
        string = ""

        #тут я создаю словарь, в котором ключ это цифра, на которую будет заменено слово в изначальной строке с
        #помощью replace, а также заполняется string, которя содержит номера, которые должны попасться, чтобы
        #это означало, что последовательность слов найдена
        for ind, word in enumerate(words):
            if word not in mass_flag:
                mass_flag.append(word)
                dict_word[f"{ind}"] = word
                string += str(ind)
                s = s.replace(word, f"{ind}")
            else:
                for key, word_d in dict_word.items():
                    if word == word_d:
                        string += key
                        break

        res, length, s_ = [], 0, ""

        s += "="
        #создаем первую последовательность символов для проверки
        for j in range(len(words)):
            s_ += s[j]
        #основной цикл, в нем, мы проходим по всей строке, перезаписывая s_ и сравниваем со string, если все символы
        #которые есть в string есть в s_, то это значит, что мы нашли последовательность, запимываем ее индекс в res
        for i in range(len(words), len(s)):
            flag = 1
            for sim in string:
                if string.count(sim) != s_.count(sim):
                    flag = 0
                    break
            if flag: res.append(length)
            length += 1 if s_[0] not in dict_word else len(dict_word[s_[0]])
            s_ = s_[1:] + s[i]

        return res


instance = Solution()
print(instance.findSubstring(s="lingmindraboofooowingdingbarrwingmonkeypoundcake", words=["fooo", "barr", "wing", "ding", "wing"]))
