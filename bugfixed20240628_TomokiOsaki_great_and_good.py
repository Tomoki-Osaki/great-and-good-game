import random

def receive_user_answer(digits: int) -> list[int]:
    """
    digits: 桁数
    ユーザーから入力を受け取り、それがdigits個の数字である場合に、入力をリストにして返す。(input(123)->[1,2,3])
    """
    while True:
        user_input = input(f'{digits}桁の数値を入力してください: ')
        try:
            user_answer = [int(i) for i in user_input] # 入力を1文字ずつ整数型にし、リストに格納する
        except ValueError: # 入力に数字以外が含まれている場合、再入力を要求する(全角数字の場合でもエラーなくプログラムは動く)
            print('全て数字で入力してください。\n')
            continue
            
        if len(user_input) == digits and len(set(user_input)) != digits:
            print(f'{digits}個の数字は重複しないようにしてください。\n')
        elif len(user_input) != digits:
            print(f'入力は{digits}桁にしてください。\n')
        else:
            break
        
    return user_answer

def game_loop(digits: int = 3, chances: int = 10) -> None:
    """
    digits: 正解の桁数
    chances: チャレンジできる回数
    """
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    right_answer = random.sample(nums, digits) # ランダムにdigitsの数だけ重複無しでnumsから数字を取得してリストにする
    print('Great&Goodを開始します!')
    num_of_trials = 0
    
    continue_game = True
    while continue_game:
        num_of_trials += 1
        print(f'{num_of_trials}回目のチャレンジ！')
        user_answer = receive_user_answer(digits=digits)
        great = 0
        good = 0
        
        for i, ans in zip(range(len(user_answer)), user_answer):
            # 数字も桁も一致している場合、greatのカウントを1増やす
            if user_answer[i] == right_answer[i]:
                great += 1
                # greatのカウント数がright_answerの要素数（桁数）と一致している場合、ゲームを終了する
                if great == len(right_answer):
                    print('正解です！！\n')
                    continue_game = False
            else:
                # 数字は一致しているが桁が不一致の場合、goodのカウント数を1増やす
                if ans in right_answer:
                    good += 1
        
        if continue_game:
            print(f'Great: {great}')
            print(f'Good: {good}\n')
        
            chances -= 1
        
            # chancesが0の場合、ユーザーに正解を伝えゲームを終了する
            if chances == 0:
                right_answer = ''.join(map(str, right_answer)) # リストの要素を結合して1つの文字列にする(例:[1,2,3]->'123')
                print(f'残念でした。答えは{right_answer}です。\n')
                continue_game = False
        
if __name__ == '__main__':
    game_loop(digits=3, chances=10)
    
