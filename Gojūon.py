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
    print("\n1. ひらがな\t2.カタカナ\t3.すべて")
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

    while True:
        cls()
        x = random.choice(candidates)
        kanas = [x["hiragana"], x["katakana"]]
        if 1 <= remember_type <= 2:
            print(kanas[remember_type - 1])
        else:
            print(kanas[random.randint(0, 1)])
        pronunciation = input("ローマ人: ")
        if pronunciation == x["pronunciation"]:
            print("✔")
        else:
            print("❌")
            print(f"({x['hiragana']} {x['katakana']} {x['pronunciation']})")
            input("何かキーを押すと続行します")


if __name__ == '__main__':
    main()
