import random
import string


class RandomWordGenerator:
    def __init__(self, num_chars: int):
        # num_charsが0未満のときTypeErrorを発生
        if not isinstance(num_chars, int):
            raise TypeError("num_chars must be an integer")
        # 整数以外のときValueErrorを発生
        if num_chars <= 0:
            raise ValueError("num_chars must be greater than 0")
        self.__num_chars = num_chars  # 文字数
        self.__lowercase_letters = string.ascii_lowercase  # a-z
        self.__uppercase_letters = string.ascii_uppercase  # A-Z
        self.__digits = string.digits  # 0-9
        self.__result = ""  # 生成された文字列を格納する変数

    def __get_num_chars(self) -> int:
        """ 生成する文字数を取得する """
        return self.__num_chars

    def __get_lower_char(self) -> str:
        """ a-zからランダムに選んだ文字列を取得する """
        return random.choice(self.__lowercase_letters)

    def __get_upper_char(self) -> str:
        """ A-Zからランダムに選んだ文字列を取得する """
        return random.choice(self.__uppercase_letters)

    def __get_digits_char(self) -> str:
        """ 0-9からランダムに選んだ文字列を取得する """
        return random.choice(self.__digits)

    def get_result(self) -> str:
        """ 生成された文字列を取得する """
        return self.__result

    def __reset_result(self) -> None:
        """ __resultを空にする """
        self.__result = ""

    def __add_result(self, word: str) -> None:
        """ ランダムに選ばれた文字列を__resultに挿入する """
        self.__result = "".join([self.__result, word])

    def run(self) -> None:
        """ 指定された文字数分の文字列を生成する """
        self.__reset_result()
        for _ in range(self.__get_num_chars()):
            # 1-3の間でランダムに整数を生成
            case = random.randint(1, 3)
            if case == 1:
                self.__add_result(self.__get_lower_char())
            elif case == 2:
                self.__add_result(self.__get_upper_char())
            elif case == 3:
                self.__add_result(self.__get_digits_char())


if __name__ == '__main__':
    pass
