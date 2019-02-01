class PythonProgrammer3:
    """DocString"""

    language = "Python"
    number_of_developers = 0

    def __init__(self, firstname, lastname):
        self.first_name = firstname
        self.last_name = lastname
        self.email = f"{firstname}.{lastname}@python.com"

        PythonProgrammer3.number_of_developers += 1

    def speak(self):
        print(f"{self.first_name} speak {self.language}")

    @classmethod
    def set_language(cls, lang):
        cls.language = lang


py_dev_1 = PythonProgrammer3("Clark", "Kent")
py_dev_2 = PythonProgrammer3("Peter","Parker")
py_dev_3 = PythonProgrammer3("Peter","Parker")

print(py_dev_1.language)
print(py_dev_1.language)
print(PythonProgrammer3.number_of_developers)

py_dev_1.set_language("Java")
print(py_dev_1.language)
