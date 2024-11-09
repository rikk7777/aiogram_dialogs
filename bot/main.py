import operator
from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message, User
from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.text import Const, Format, List, Multi
from environs import Env
from aiogram_dialog.widgets.kbd import Url, Column, Radio
from aiogram_dialog.widgets.media import StaticMedia
from aiogram.types import ContentType
from aiogram_dialog.widgets.input import TextInput, ManagedTextInput
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Next, Start, Cancel, SwitchTo

env = Env()
env.read_env()

BOT_TOKEN = env('BOT_TOKEN')


bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

router = Router()

class StartSG(StatesGroup):
    first = State()
    second = State()
    third = State()


class SecondDialogSG(StatesGroup):
    first = State()
    second = State()


start_dialog = Dialog(
    Window(
        Const('<b>Вы находитесь в первом окне первого диалога</b>\n'),
        Const('Вы можете переключаться между окнами текущего диалога, '
              'или перейти в новый 👇'),
        Row(
            SwitchTo(Const('2️⃣'), id='w_second', state=StartSG.second),
            SwitchTo(Const('3️⃣'), id='w_third', state=StartSG.third),
        ),
        Start(Const('Во 2-й диалог ▶️'), id='go_second_dialog', state=SecondDialogSG.first),
        state=StartSG.first
    ),
    Window(
        Const('<b>Вы находитесь во втором окне первого диалога</b>\n'),
        Const('Вы можете переключаться между окнами текущего диалога, '
              'или перейти в новый 👇'),
        Row(
            SwitchTo(Const('1️⃣'), id='w_first', state=StartSG.first),
            SwitchTo(Const('3️⃣'), id='w_third', state=StartSG.third),
        ),
        Start(Const('Во 2-й диалог ▶️'), id='go_second_dialog', state=SecondDialogSG.first),
        state=StartSG.second
    ),
    Window(
        Const('<b>Вы находитесь в третьем окне первого диалога</b>\n'),
        Const('Вы можете переключаться между окнами текущего диалога, '
              'или перейти в новый 👇'),
        Row(
            SwitchTo(Const('1️⃣'), id='w_first', state=StartSG.first),
            SwitchTo(Const('2️⃣'), id='w_second', state=StartSG.second),
        ),
        Start(Const('Во 2-й диалог ▶️'), id='go_second_dialog', state=SecondDialogSG.first),
        state=StartSG.third
    ),
)


second_dialog = Dialog(
    Window(
        Const('<b>Вы находитесь в первом окне второго диалога!</b>\n'),
        Const('Нажмите на кнопку Отмена,\nчтобы вернуться в стартовый диалог 👇'),
        SwitchTo(Const('2️⃣'), id='w_second', state=SecondDialogSG.second),
        Cancel(Const('Отмена'), id='button_cancel'),
        state=SecondDialogSG.first
    ),
    Window(
        Const('<b>Вы находитесь во втором окне второго диалога!</b>\n'),
        Const('Нажмите на кнопку Отмена,\nчтобы вернуться в стартовый диалог 👇'),
        SwitchTo(Const('1️⃣'), id='w_first', state=SecondDialogSG.first),
        Cancel(Const('Отмена'), id='button_cancel'),
        state=SecondDialogSG.second
    ),
)

@dp.message(CommandStart())
async def command_start_process(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(
        state=StartSG.first,
        mode=StartMode.RESET_STACK,
        data={'first_show': True}
    )

dp.include_router(router)
dp.include_router(start_dialog)
dp.include_router(second_dialog)
setup_dialogs(dp)
dp.run_polling(bot)