import tkinter as tk
import tkinter.messagebox as messagebox
from random_generator import RandomWordGenerator


class MyApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("RandomWordGenerator")  # タイトル
        self.master.geometry("200x100")  # ウィンドウサイズ
        self.text_box = None  # 生成する文字数入力用エントリ
        self.result_box = None  # 生成結果表示ラベル
        self.__create_widget()

    def __create_widget(self) -> None:
        """ 各ウィジェットを生成・配置する """

        num_label = tk.Label(
            self.master,
            text="生成する文字数"
        )
        num_label.place(
            x=30,
            y=10
        )

        # 生成する文字数入力用エントリ
        self.text_box = tk.Entry(
            self.master,
            width=4
        )
        # 初期値:8
        self.text_box.insert(0, "8")
        self.text_box.place(
            x=120,
            y=10
        )

        # 生成ボタン
        generate_button = tk.Button(
            self.master,
            width=7,
            text="生成",
            command=self.__generate_text
        )
        generate_button.place(
            x=30,
            y=40
        )

        # コピーボタン
        copy_button = tk.Button(
            self.master,
            width=7,
            text="コピー",
            command=self.__copy_text
        )
        copy_button.place(
            x=100,
            y=40
        )

        result_label = tk.Label(
            self.master,
            text="生成された文字"
        )
        result_label.place(
            x=5,
            y=70
        )

        # 生成結果表示用エントリ
        self.result_box = tk.Entry(
            self.master,
            width=15
        )
        self.result_box.place(
            x=90,
            y=70
        )

    def __generate_text(self) -> None:
        """ 指定した文字数の文字列を生成する """
        self.__delete_result_box()
        rwg = RandomWordGenerator(int(self.__get_text_box()))
        rwg.run()
        self.__insert_result_box(rwg.get_result())

    def __copy_text(self) -> None:
        """ 生成された文字列をクリップボードにコピーする """
        self.master.clipboard_clear()  # クリップボードをクリア
        self.master.clipboard_append(self.__get_result_box())  # クリップボードにテキストを追加
        messagebox.showinfo("コピー", "生成された文字をコピーしました")  # メッセージボックスに表示

    def __get_text_box(self):
        return self.text_box.get()

    def __get_result_box(self) -> str:
        """
        result_boxの中身を取得する
        Returns:
            str: 生成された文字列
        """
        return self.result_box.get()

    def __delete_result_box(self) -> None:
        """ result_boxを空にする """
        self.result_box.delete(0, tk.END)

    def __insert_result_box(self, char: str) -> None:
        """
        result_boxに生成された文字列を挿入する

        Args:
            char(str): 生成された文字列
        """
        self.result_box.insert(0, char)


if __name__ == "__main__":
    root = tk.Tk()
    app = MyApplication(root)
    root.mainloop()
