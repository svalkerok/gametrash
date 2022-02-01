from random import random, randrange, randint
import time
import ctypes



name = "Seed"
def lavka():
    while True:
        w = input('Введите "1", чтобы пойти в лавку, или введите "2", чтобы отправиться в казарму: ')
        if w == "1":
            print("Вы вошли в лавку оружейника. Перед вами на выбор обычный и удобный меч, и большой двуручный длинный меч.")
            print("Выберите нужное число: ")
            ww = input("1 - меч, 2 - двуручный меч: ")
            if ww == "1":
                weapon = "меч"
                print("Вы выбрали меч.")
                return weapon
            elif ww == "2":
                print("Вы выбрали двуручный меч")
                weapon = "двуручный меч"
                return weapon
            else:
                if w == '':
                    print('Вы ничего не ввели.')
                    time.sleep(1)
                    continue
                else:
                    print("Вы ввели неверное значение.")
                    time.sleep(1)
                    continue
        elif w == "2":
            print("Вы вошли в городскую казарму, где вам смогли выдать только обычное копье")
            weapon = "копье"
            return weapon
        else:
            if w == '':
                print('Вы ничего не ввели.')
                time.sleep(1)
                continue
            else:
                print("Вы ввели неверное значение.")
                time.sleep(1)
                continue
            

weapon = lavka()

print(f"Так как {name} выбрал {weapon}, он решает сразу же отправиться к логову мерзских гоблинов.")
print(f"Пройдя длинный путь, {name} предстал перед входом в пещеру, в которой обитают гоблины.")
print(f"Держа в руках {weapon}, {name} окончательно решает, входить ему в пещеру, или нет")

health = 100
print("Пройдя немного дальше, вы увидели перед собой животное, внешне напоминающее дикого кабана.")
print("Как только животное заметило вас, оно стремительно начало атаку.")
def kaban():
    kaban_hp = 100
    while kaban_hp > 0:
        if kaban_hp > 50:
            print("1 - Удар с выпадом, 2 - Сильный удар с замахом.")
            hit = randint(1, 10)
            hit1 = randint(5, 15)
            nn = input('> ')
            if nn == "1":
                print(f'Нанесен удар с выпадом, кабан теряет {hit} очков здоровья.')
                kaban_hp = kaban_hp - hit
                print(f'Текущий уровень здоровья кабана - {kaban_hp}.')
            elif nn == "2":
                print(f'Нанесен сильный удар с замахом, кабан теряет {hit1} очков здоровья.')
                kaban_hp = kaban_hp - hit1
                print(f'Текущий уровень здоровья кабана - {kaban_hp}.')
            else:
                print('Мимо.(')
                continue
        elif kaban_hp < 50:
            print('1 - Критический колющий удар, 2 - Критический рубящий удар.')
            hit2 = randint(10, 20)
            hit3 = randint(10, 15)
            nnn = input('> ')
            if nnn == "1":
                print(f'Нанесен критический колющий удар, кабан теряет {hit2} здоровья.')
                kaban_hp = kaban_hp - hit2
                print(f'Текущий уровень здоровья кабана - {kaban_hp}.')
            elif nnn == '2':
                print(f'Нанесен рубящий удар с критическим уроном, кабан теряет {hit3} здоровья.')
                kaban_hp = kaban_hp - hit3
                print(f'Текущий уровень здоровья кабана - {kaban_hp}.')
            else:
                print('Мимо. :((')
                continue
        else:
            print('Мимо.:(')
            continue
kaban()
print(f"Уровень вашего здоровья - {health}")

def kabanhp():
    kaban_hp = 100

