from sys import argv
from datetime import datetime


def get_weekday_title(index):
    weekdays = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
    return weekdays[index]


def print_task_weekday(tasks, start_index):
    """指定された曜日から始まるタスクを順に表示する関数

    Args:
        tasks (_type_): 引数
        start_index (_type_): _description_
    """
    for i in range(7):
        index = (start_index + i) % 7
        title = get_weekday_title(index)
        print(f'{title}: {tasks[index]}')


def main(args):
    """現在の曜日を取得

    Args:
        args (_type_): task引数を設定
    """
    current_weekday = datetime.now().weekday()

    tasks = args

    print_task_weekday(tasks, current_weekday)


if __name__ == '__main__':
    """日数の数が正しくない場合はエラーメッセージ
    """
    if len(argv) != 8:
        print('曜日毎のタスクを７つ入力してください')
        exit(1)

    """メイン関数を呼び出し
    """
    main(argv[1:])