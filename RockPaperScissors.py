import discord
from discord.ext import commands
import random

# Создаем бот

bot = commands.Bot(command_prefix='!')

# Определяем возможные варианты
choices = ["камень", "ножницы", "бумага"]

@bot.event
async def on_ready():
    print(f'Запущен бот: {bot.user.name}')

@bot.command()
async def rps(ctx, choice: str):
    choice = choice.lower()
    if choice not in choices:
        await ctx.send("Пожалуйста, выбери между камень, ножницы или бумага.")
        return

    bot_choice = random.choice(choices)
    await ctx.send(f'Я выбрал: {bot_choice}')

    # Логика выигрыша
    if choice == bot_choice:
        await ctx.send("Ничья!")
    elif (choice == "камень" and bot_choice == "ножницы") or (choice == "ножницы" and bot_choice == "бумага") or (choice == "бумага" and bot_choice == "камень"):
         
         
        await ctx.send("Ты выиграл!")
    else:
        await ctx.send("Я выиграл!")


bot.run('Это я помню что удалять надо :)')
