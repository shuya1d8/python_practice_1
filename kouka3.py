# 現在の日付と時刻を取得
import datetime

# ランダム
import random


# ================================================================================================
# 現在の時刻等
NOW_DATETIME = datetime.datetime.now()                   # 現在の年月日時間
NOW_TIME = NOW_DATETIME.strftime('%H時%M分')             # 現在の?時?分
NOW_HOUR = NOW_DATETIME.hour                             # 現在の時
NOW_DATE = NOW_DATETIME.strftime('%m月%d日')             # 現在の?月?日
DAYS = datetime.date.today().weekday()                   # 現在の曜日

# ランダムな数
RAND = random.randint(1000, 9999)
# RAND = random.randint(1000, 1000)    #テスト用


# ================================================================================================
# 開発者情報
class DEVELOPER:
    def __init__(self, no: int, name: str) -> None:
        """コンストラクタ"""
        self.__no = no
        self.__name = name

    def dsply(self):
        print('===開発者情報===')
        print('No.{}'.format(self.__no))
        print('名前：{}'.format(self.__name))


# 開発者 インスタンス化
no_1 = DEVELOPER(1, '太田秀弥')
# no_2 = DEVELOPER(, '')
# no_3 = DEVELOPER(, '')


# ================================================================================================
# あいさつの表示(4時~9時59分:おはようございます/10時~18時59分:こんにちは/19時~3時59分:こんばんは)
def greeting():
    if 4 <= NOW_HOUR <= 9:
        print('おはようございます', end='')
    elif 10 <= NOW_HOUR <= 18:
        print('こんにちは', end='')
    else:
        print('こんばんは', end='')

# 曜日の変換
def day():
    if DAYS == 0:
        return '月'
    elif DAYS == 1:
        return '火'
    elif DAYS == 2:
        return '水'
    elif DAYS == 3:
        return '木'
    elif DAYS == 4:
        return '金'
    elif DAYS == 5:
        return '土'
    elif DAYS == 6:
        return '日'

# txtファイル処理 (書き込み用open→書き込み→読み取り用open/////読み取りはそれぞれで)
def txt_file(file_name, txt_mode, file_write):
    txt_f = open(file_name, txt_mode)
    txt_f.write(file_write)
    txt_f = open(file_name)
    return txt_f


# ================================================================================================
# マスター名入力
name = input('名前を入力してください：')
# name = '制作者'
master = str(name) + '様'

# txtファイル処理　書き込み&読み取り
txt_f = txt_file('name.txt', 'w', 'kouka3マシン・・・起動しました')
line1 = txt_f.readline()
print('===== {} ====='.format(line1))
txt_f.close()

# あいさつ
greeting()
print('、{}。'.format(master))

# -----------------------------------------------------------------------------

# 機能
count = 0
print('本日は何をしましょうか。')
while True:
    # 正常動作
    try:
        # 機能選択
        while True:
            if count > 0:
                print('何をしましょうか。')
            print('実装機能一覧[ 0:終了/ 1:今日の日付/ 2:起動時刻/ 3:計算/ 999:開発者一覧]')
            instruct = int(input('入力：'))
            print()

            if instruct in {0, 1, 2, 3, 999, RAND}:
                break
            else:
                print('申し訳ございません、その機能は実装されていません。')
                print()
                continue

        # 機能0 実行終了
        if instruct == 0:
            print('終了いたします。\nおやすみなさいませ、{}。'.format(master))
            break

        # 機能1 今日の日付
        elif instruct == 1:
            count += 1
            print('本日は{}{}曜日です。'.format(NOW_DATE, day()))
            print()
            continue

        # 機能2 起動時刻
        elif instruct == 2:
            count += 1
            print('起動時刻は{}です。'.format(NOW_TIME))
            print()
            continue

        # 機能3 計算
        elif instruct == 3:
            count += 1
            while True:
                while True:
                    try:
                        print('現在行える計算は10進数の「1:足し算」「2:引き算」「3:掛け算」「4:割り算」です。「0:戻る」')
                        sel_cal = int(input('どの計算を行いますか（指定しない場合は「5」)：'))
                        if sel_cal in {0, 1, 2, 3, 4, 5}:
                            print()
                            break
                        else:
                            print('無効な値です。')
                            print()
                    except Exception:
                        print('無効な値です。')
                        print()
                        continue
            
                # 戻る
                if sel_cal == 0:
                    break

                # 足し算
                if sel_cal == 1:
                    print('足す数を入力してください。終了の場合は「=」を入力してください。末尾の値を消去したい場合は「del」と入力してください。')
                    sum_lst = []
                    total = 0
                    while True: 
                        num = input('実数値：')

                        # 入力終了
                        if num == '=' or num == '＝':
                            try:
                                # 計算
                                if sum_lst:
                                    total = sum(sum_lst)
    
                                print('計算結果 --> {:g}'.format(total))
                                print()
                                
                            except:
                                print()
                                continue

                            break

                        try:
                            # 値消去
                            if num == 'del':
                                del sum_lst[-1]
                                print('[', ' + '.join([str(_) for _ in sum_lst]), ']', sep='')
                                continue

                            # リスト追加&表示
                            sum_lst.append(float(num))
                            print('[', ' + '.join([str(_) for _ in sum_lst]), ']', sep='')
                        except:
                            print('無効な値です。計算には含まれません。')
                            print('[', ' + '.join([str(_) for _ in sum_lst]), ']', sep='')
                            continue

                # 引き算
                elif sel_cal == 2:
                    print('引く数を入力してください。終了の場合は「=」を入力してください。末尾の値を消去したい場合は「del」と入力してください。')
                    sub_lst = []
                    total = 0
                    while True: 
                        num = input('実数値：')

                        # 入力終了
                        if num == '=' or num == '＝':
                            try:
                                # 計算
                                if sub_lst:
                                    total = sub_lst[0] * 2
                                    for i in range(len(sub_lst)):
                                        total -= sub_lst[i]

                                print('計算結果 --> {:g}'.format(total))
                                print()
                            except:
                                print()
                                continue

                            break

                        try:
                            # 値消去
                            if num == 'del':
                                del sub_lst[-1]
                                print('[', ' - '.join([str(_) for _ in sub_lst]), ']', sep='')
                                continue

                            # リスト追加&表示
                            sub_lst.append(float(num))
                            print('[', ' - '.join([str(_) for _ in sub_lst]), ']', sep='')
                        except:
                            print('無効な値です。計算には含まれません。')
                            print('[', ' - '.join([str(_) for _ in sub_lst]), ']', sep='')
                            continue

                # 掛け算
                elif sel_cal == 3:
                    print('掛ける数を入力してください。終了の場合は「=」を入力してください。末尾の値を消去したい場合は「del」と入力してください。')
                    mul_lst = []
                    total = 0
                    while True: 
                        num = input('実数値：')

                        # 入力終了
                        if num == '=' or num == '＝':
                            try:
                                # 計算
                                if mul_lst:
                                    total = 1
                                    for i in range(len(mul_lst)):
                                        total *= mul_lst[i]

                                print('計算結果 --> {:g}'.format(total))
                                print()
                            except:
                                print()
                                continue

                            break

                        try:
                            # 値消去
                            if num == 'del':
                                del mul_lst[-1]
                                print('[', ' × '.join([str(_) for _ in mul_lst]), ']', sep='')
                                continue

                            # リスト追加&表示
                            mul_lst.append(float(num))
                            print('[', ' × '.join([str(_) for _ in mul_lst]), ']', sep='')
                        except:
                            print('無効な値です。計算には含まれません。')
                            print('[', ' × '.join([str(_) for _ in mul_lst]), ']', sep='')
                            continue

                # 割り算
                elif sel_cal == 4:
                    print('割る数を入力してください。終了の場合は「=」を入力してください。末尾の値を消去したい場合は「del」と入力してください。')
                    print('※ 計算の途中で割り切れない数字がでる場合はその都度余りは無視されて計算されます。')
                    div_lst = []
                    total = 0
                    other_total = 0
                    remainder = 0
                    while True: 
                        num = input('実数値：')

                        # 入力終了
                        if num == '=' or num == '＝':
                            try:
                                # 計算
                                if div_lst:
                                    total = div_lst[0]**2
                                    other_total = div_lst[0]**2
                                    for i in range(len(div_lst)):
                                        remainder = total % div_lst[i]
                                        total //= div_lst[i]
                                        other_total /= div_lst[i]

                                print('計算結果 --> {:g} ///または/// {:g} あまり {:.10g}'.format(other_total, total, remainder))
                                print()
                            except ZeroDivisionError as zd_e:
                                # 0の除算
                                print('0の除算が行われました。')
                                while True:
                                    corr_sel = input('修正しますか？「Yes:y」「No:n」：')
                                    yes_flg = True
                                    if corr_sel == 'y' or corr_sel == 'Y':
                                        break
                                    elif corr_sel == 'n' or corr_sel == 'N':
                                        yes_flg = False
                                        break
                                    else:
                                        print('無効な値です。')
                                        continue

                                # 0の除算どうする？    
                                if yes_flg:
                                    while 0 in div_lst:
                                        div_lst.remove(0)
                                    print('[', ' ÷ '.join([str(_) for _ in div_lst]), ']', sep='')
                                    continue
                                else:
                                    div_lst.clear()
                                    total = 0
                                    other_total = 0
                                    remainder = 0
                                    print('割る数を入力してください。終了の場合は「=」を入力してください。末尾の値を消去したい場合は「del」と入力してください。')
                                    print(div_lst)
                                    continue
                            except:
                                print()

                            break

                        try:
                            # 値消去
                            if num == 'del':
                                del div_lst[-1]
                                print('[', ' ÷ '.join([str(_) for _ in div_lst]), ']', sep='')
                                continue

                            # リスト追加&表示
                            div_lst.append(float(num))
                            print('[', ' ÷ '.join([str(_) for _ in div_lst]), ']', sep='')
                        except:
                            print('無効な値です。計算には含まれません。')
                            print('[', ' ÷ '.join([str(_) for _ in div_lst]), ']', sep='')
                            continue

                # 指定なし計算
                elif sel_cal == 5:
                    # print('値を入力してください。終了の場合は「=」を入力してください。末尾の値を消去したい場合は「del」と入力してください。')
                    # print('演算子はそれぞれに対応している数字（「+：1」「-：2」「×：3」「÷：4」）を入力してください。')
                    # cal_lst = []
                    # while True: 
                    #     num = input('実数値：')

                    #     # 入力終了
                    #     if num == '=' or num == '＝':
                    #         break
            
                    print('申し訳ございません、まだ未実装です。')
                    print()
                    continue

        # 機能999 開発者一覧
        elif instruct == 999:
            count += 1
            no_1.dsply()
            print()
        
        # 機能random ランダム
        elif instruct == RAND:
            count += 1
            # 到達者の記録
            # txtファイル処理　書き込み
            txt_f = txt_file('rand.txt', 'a', '{}\n'.format(name))

            print('おめでとうございます。')
            print('{}は見事シークレット機能にたどり着きました。'.format(master))
            print('本日の運勢は絶好調のようですね。')
            print('では、ごきげんよう。')
            print()

            # 歴代到達者一覧表示
            print('=歴代到達者==========')

            # txtファイル処理　読み取り
            for line in txt_f:
                print(' ', end='')
                print(line, end='')
            txt_f.close()

            print('=====================')
            print()

            continue

        # 無効な値
        else:
            print('無効な値です。')
            print()
    
    # 例外処理　キー割り込み
    except KeyboardInterrupt:
        print()
        print('強制終了します。')
        exit()
    
    # 例外処理　システム終了以外のすべての例外クラスの基底クラス
    except Exception as e:
        print()
        print('エラーが発生しました。{}'.format(type(e)))
        print()

    # 例外処理　その他(予備)
    except:
        print()
        print('エラーが発生しました。')
        print()
        break
