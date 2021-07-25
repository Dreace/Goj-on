import json
import os
import random


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    with open("data.json", encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    for index, line in enumerate(data):
        print(f"{index + 1}. ", end='')
        for hiragana in line["hiragana"]:
            print(hiragana, end=' ')
        print("\n   ", end='')
        for katakana in line["katakana"]:
            print(katakana, end=' ')
        print()
    print("\n1. ひらがな  2.カタカナ  3.すべて")
    remember_type = int(input("モードを選択: "))
    input_text = input("\n行を選択: ")
    indexes = []
    for x in input_text.split(","):
        if x.find("-") != -1:
            indexes += list(range(int(x.split('-')[0]) - 1, int(x.split('-')[1])))
        else:
            indexes.append(int(x) - 1)
    candidates = []
    for index in indexes:
        for i in range(5):
            candidates.append({
                "hiragana": data[index]["hiragana"][i],
                "katakana": data[index]["katakana"][i],
                "pronunciation": data[index]["pronunciation"][i],
            })
    total_count = 1e-10
    correct_count = 0
    while True:
        cls()
        print(f"正しいレート: {correct_count / total_count * 100:.2f}% ({correct_count}/{int(total_count)})")
        print("\n")
        x = random.choice(candidates)
        kanas = [x["hiragana"], x["katakana"]]
        print("仮名:",end=' ')
        if 1 <= remember_type <= 2:
            print(f"\033[91m{kanas[remember_type - 1]}\033[00m")
        else:
            print(f"\033[91m{kanas[random.randint(0, 1)]}\033[00m")
        pronunciation = input("ローマ人: ")
        if pronunciation == x["pronunciation"]:
            print("✔")
            correct_count += 1
        else:
            print("❌")
            print(f"({x['hiragana']} {x['katakana']} {x['pronunciation']})")
            input("何かキーを押すと続行します")
        total_count += 1


if __name__ == '__main__':
    main()
