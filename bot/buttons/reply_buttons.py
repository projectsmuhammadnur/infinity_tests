import json

import requests
from aiogram.types import ReplyKeyboardMarkup

from bot.buttons.text import back_main_menu, adverts, none_advert, forward_advert, performance, cabinet, end_test, \
    choice_language, choice_language_ru, cabinet_ru, performance_ru, end_test_ru


async def main_menu_buttons(chat_id: int):
    tg_user = json.loads(requests.get(url=f"http://127.0.0.1:8000/api/telegram-users/chat_id/{chat_id}/").content)
    if tg_user['language'] == 'uz':
        design = [
            [cabinet, performance],
            [choice_language]
        ]
    else:
        design = [
            [cabinet_ru, performance_ru],
            [choice_language_ru]
        ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


async def back_main_menu_button():
    design = [[back_main_menu]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


async def admin_menu_buttons():
    design = [
        [adverts],
        [back_main_menu]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


async def advert_menu_buttons():
    design = [
        [none_advert, forward_advert],
        [back_main_menu]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


async def test_performance_menu_button(test: dict, chat_id: int):
    tg_user = json.loads(requests.get(url=f"http://127.0.0.1:8000/api/telegram-users/chat_id/{chat_id}/").content)
    design = []
    for i in test['answers']:
        design.append([i['answer']])
    if tg_user['language'] == 'uz':
        design.append([end_test])
    else:
        design.append([end_test_ru])
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)