import random

globalLife = 5;

def RandomWord():
    with open("Words.txt","r",encoding="utf-8") as f:
        words = (f.read().split("\n"));

    f.close();

    return words[random.randint(0,len(words) - 1)];

def HideWord(word : str):
    wordChars = [];

    for i in range(len(word)):
        wordChars.append("_");

    return "".join(wordChars);

def Show(symbol : str,hide : str,word : str):
    li = list(hide);

    for i in range(len(li)):
        if (symbol.lower() == word[i].lower()):
            li[i] = word[i];

    return "".join(li);

def Compare(srt1: str, str2: str):
    return srt1 == str2;

def OverGame(hide : str,word : str,life : int):

    if (life <= 0):
        print("Вы проиграли!");
        print("Загаданное слово было : " + word);
    elif hide.find("_") == -1:
        print("Загаданное слово : " + hide);
        print("Вы победили!");
        life = 0;

    return  life;

def Game():
    word = RandomWord();
    hide = HideWord(word);
    life = globalLife;

    while life != 0:
        print("Мы загадали слово");
        print("Загаданное слово : " + hide + " у вас есть " + str(life) + " попытки!");
        print("Я думаю в этом слове есть буква...");
        symbol = input()
        newhide = Show(symbol, hide, word);

        if (Compare(hide,newhide) == True):
            life -= 1;

        hide = newhide;
        life = OverGame(hide,word, life);


if __name__ == '__main__':
    Game();