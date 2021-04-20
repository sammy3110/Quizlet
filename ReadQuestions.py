class Questions:
    def __init__(self):
        pass
        
    def fetchQuestions(self):
        file = open("Questions.txt", "r")
        v = []
        for each in file.readlines():
            v.append(each.rstrip('\n'))

        dict_q = {}
        flag = 1
        for each in v:
            dict_q[flag] = each.split('_')
            flag+=1
        return dict_q