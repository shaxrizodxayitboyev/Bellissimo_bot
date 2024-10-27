from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from utils.db_api.db_code import ProductDB

product_cb = CallbackData('product', 'product_id', 'count', 'action')
item_cb = CallbackData('product', 'count', 'action')


def plus_minus(product_id, count):
    inline = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='-',
                              callback_data=product_cb.new(product_id=product_id, count=count, action='minus')),
         InlineKeyboardButton(text=str(count),
                              callback_data=product_cb.new(product_id=product_id, count=count, action='count')),
         InlineKeyboardButton(text='+',
                              callback_data=product_cb.new(product_id=product_id, count=count, action='plus'))],
        [InlineKeyboardButton(text='Savatga qo`shish',
                              callback_data=product_cb.new(product_id=product_id, count=count, action='save'))]
    ])
    return inline


def basket_buttons(user_id, count):
    products = ProductDB().get(user_id=user_id)
    inline_button = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='-', callback_data=item_cb.new(count=count, action='minus_basket')),
         InlineKeyboardButton(text="Kartoshkali",
                              callback_data=item_cb.new(count=count, action='kartoshkali')),
         InlineKeyboardButton(text='+', callback_data=item_cb.new(count=count, action='plus_basket'))]
    ])

    return inline_button
