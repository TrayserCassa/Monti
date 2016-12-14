import time


class PrettyPrint():
    def __init__(self, delay, max_lines, max_length):
        self.max_length = max_length
        self.max_lines = max_lines
        self.message = None
        self.delay = delay

    def print(self, string):
        self.message = self.split_return(string)

        print(self.message)

    def split_return(self, string):
        mes = string.split("\n")

        if len(mes) > self.max_lines:
            raise ValueError("Too many returns in string!")

        for i in range(len(mes)):
            mes[i] = mes[i].strip()

        return mes

    def _ausgabe(message):
        print(message)


if __name__ == "__main__":
    p = PrettyPrint(5, 4, 10)
    p.print("Hallo das ist \n ein kleiner \n Test von dem neuem Tool")
