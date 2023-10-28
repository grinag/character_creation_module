"""Game module with characteristics."""

from random import randint
from graphic_arts.start_game_banner import run_screensaver


def attack(char_name: str, char_class: str) -> str:
    """Damage depend on class of gamer."""
    if char_class == 'warrior':
        aa: int = 3
        bb: int = 5
    if char_class == 'mage':
        aa: int = 5
        bb: int = 10
    if char_class == 'healer':
        aa: int = -3
        bb: int = -1
    return f'{char_name} нанёс урон противнику равный {5 + randint(aa, bb)}'


def defence(char_name: str, char_class: str) -> str:
    """Defence depend on class of gamer."""
    if char_class == 'warrior':
        aa: int = 5
        bb: int = 10
    if char_class == 'mage':
        aa: int = -2
        bb: int = 2
    if char_class == 'healer':
        aa: int = 2
        bb: int = 5
    return f'{char_name} блокировал {10 + randint(aa, bb)} урона'


def special(char_name: str, char_class: str) -> str:
    """Choice of strike depending on the character class."""
    if char_class == 'warrior':
        aa: int = 80
        bb: int = 25
        skill: str = f'Выносливость {aa + bb}'
    if char_class == 'mage':
        aa: int = 5
        bb: int = 40
        skill: str = f'Атака {aa + bb}'
    if char_class == 'healer':
        aa: int = 10
        bb: int = 30
        skill: str = f'Защита {aa + bb}'
    return f'{char_name} применил специальное умение «{skill}»'


def start_training(char_name: str, char_class: str) -> str:
    """Definition depend on class of gamer."""
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника,\
          defence — ')
    print('чтобы блокировать атаку противника или special — \
    чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = ''
    while cmd != 'skip':
        cmd: str = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Choice class of gamer."""
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        char_class = input('Введи название персонажа, за которого хочешь\
        играть: '
                           'Воитель — warrior, Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. Сильный, выносливый\
            и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. Обладает высоким\
            интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. Черпает силы из\
            природы, веры и духов.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор,\
        или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))