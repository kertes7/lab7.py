#task 1
import random

objects = ["кіт", "камінь", "дракон"]
answer = random.choice(objects)
attempts = 5

print("Гра: 'Здогадайся, хто я?'")
print("Підказка: Це може бути живе, неживе або вигадане...")

while attempts > 0:
    try:
        guess = input("Ваша здогадка: ").strip().lower()
        if not guess:
            raise ValueError("Порожній ввід!")

        if guess == answer:
            print("Правильно! Ви вгадали!")
            break
        else:
            print("Ні, це не те... Спробуйте ще.")
            attempts -= 1
            if random.random() > 0.5:
                print("Підказка:", "Це" + (" живе" if answer == "кіт" else " неживе" if answer == "камінь" else " вигадане"))

    except Exception as e:
        print("Щось пішло не так:", e)

if attempts == 0:
    print(f"Ви не вгадали. Це було: {answer}")

#task 2

character = {
    "ім'я": "Шерлок Холмс",
    "підказки": [
        "Я не справжній, але мене всі знають.",
        "Мій друг — доктор.",
        "Я часто ношу капелюх.",
        "Мене створив Конан Дойл."
    ]
}
import random

print("Гра: 'Хто я?'")
used_hints = []
attempts = 0

while True:
    guess = input("Хто я, на вашу думку? (або введіть 'підказка'): ").strip().lower()

    if guess == "підказка":
        available = [h for h in character["підказки"] if h not in used_hints]
        if available:
            hint = random.choice(available)
            print("Підказка:", hint)
            used_hints.append(hint)
        else:
            print("Підказок більше немає.")
    elif guess == character["ім'я"].lower():
        if random.random() > 0.5:
            print("О ні... Ви програли... (жартую, ви виграли!)")
        else:
            print("Вау! Ви вгадали! Це дійсно Шерлок Холмс!")
        break
    else:
        print("Хмм... не зовсім. Спробуйте ще.")
    attempts += 1
    if attempts > 7:
        print("Здається, гра затягнулась. Це був Шерлок Холмс.")
        break

#task 3

import random
import time

options = ["кіт", "машина", "єдиноріг", "телефон", "привид"]
real_answer = random.choice(options)

print("Гра: 'Я думаю, це... хоча, може, й ні'")
print("Виберіть, що ви хочете вгадати (але це нічого не гарантує):")
print(", ".join(options))
player_choice = input("Ваш вибір: ").strip().lower()

attempts = 0
max_attempts = random.randint(5, 10)

while True:
    guess = input("Спробуйте вгадати: ").strip().lower()

    if not guess or not guess.isalpha():
        print("Щось дивне ви написали... Але ми продовжимо.")
    else:
        give_real_hint = random.random() > 0.5
        hint = f"Це {('не ' if not give_real_hint else '')}{real_answer}"
        print("Підказка:", hint)

    attempts += 1
    time.sleep(0.5)

    if guess == real_answer:
        print("Можливо, ви вгадали... або ні. Хто знає?")
        break

    if attempts >= max_attempts:
        print("Гра завершилась... Можливо, ви щось зрозуміли?")
        break

print("Результат:", "Ви виграли!" if guess == real_answer else "Цього разу не пощастило.")

