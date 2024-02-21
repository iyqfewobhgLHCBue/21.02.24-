import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandObject
from aiogram import F
from aiogram.types import FSInputFile

#from aiogram.types import FSInputFile

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6833268368:AAEUkfps_AMX_HuL4PW1eQV3UdeN6e5Sa4s")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message, command:CommandObject):
    if command.args is None:
        await message.answer("Привет!")
        return
    else:
        await message.answer((f'Привет, {command.args}'))
@dp.message(Command("help"))
async def cmd_start(message: types.Message):
    await message.answer("city-список городов \n find-выберите город")
@dp.message(Command("city"))
async def cmd_start(message: types.Message):
    await message.answer("Казань\nМосква\nСочи\nСанкт-Питербург\nИжевск")
@dp.message(Command("find"))
async def cmd_start(message: types.Message, command:CommandObject):
    if command.args is None:
        await message.answer("передайте название города")
        return
    elif command.args == "Казань":
        await message.answer('1.Казанский кремль\n2.Мечеть Кул-Шариф\n3.АК Барс Арена\n4.Башня Сююмбике\n5.Государственный музей изобразительных искусств РТ\n6.Казанский авиационный завод имени С.П.Горбунова\n7.Мост Миллениум')
        return
    elif command.args == "Москва":
        await message.answer('1.Красная площадь и Мавзолей\n2.Московский Кремль.\n3.Алмазный фонд и Оружейная палата.\n4.Храм Василия Блаженного.\n5.Государственный исторический музей.\n6.Храм Христа Спасителя.')
        return
    elif command.args == "Сочи":
        await message.answer("1.Парк 'Ривьера'\n2.Олимпийский парк\n3.Дача Сталина\n4.Скайпарк Сочи\n5.Дольмены Красной Поляны")
        return
    elif command.args == "Санкт-Петербург":
        await message.answer("1.Эрмитаж \n2.Невский проспект\n3.Русский музей\n4.Петропавловская крепость\n5.Исаакиевский собор")
        return
    elif command.args == "Ижевск":
        await message.answer("1.Набережная зодчего Дудина.\n2.Монумент дружбы народов.\n3.Музей Калашникова.\n4.Музей завода «Ижмаш».\n5.Музей Кузебая Герда.\n6.Ижевский зоопарк.")

@dp.message(F.text.lower() == "привет")
async def cmd_start(message: types.Message):
    await message.answer("привет, я бот помощник в сфере Российских достопримечательностей")
@dp.message(F.text.lower() == "кто тебя создал?")
async def cmd_start(message: types.Message):
    await message.answer("меня создал cucumber228")
@dp.message(F.text.lower() == "на каком языке ты написан?")
async def cmd_start(message: types.Message):
    await message.answer("любопытной варваре на базаре нос оторвали")
#
# @dp.message(Command("image") == "привет")
# async def cmd_start(message: types.Message):
#     imagebot = FSInputFile("")
# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())