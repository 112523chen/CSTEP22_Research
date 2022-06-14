class Question:
    def __init__(self, id, title, prompt, question_type, python_difficulty, sql_difficulty, fileNames, company_name):
        self.id = id
        self.title = title
        self.prompt = prompt
        self.question_type = question_type
        self.python_difficulty = python_difficulty
        self.sql_difficulty = sql_difficulty
        self.fileNames = fileNames
        self.company_name = company_name

    def addFile(self, fileName):
        return self.fileNames.append(fileName)
