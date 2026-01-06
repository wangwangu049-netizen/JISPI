
import discord
from discord.ext import commands
import random
import matplotlib.pyplot as plt

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

start_value = 500  # GISPI start value

@bot.event
async def on_ready():
    print(f"봇 로그인 완료: {bot.user}")

@bot.command()
async def gispi(ctx):
    global start_value
    prices = [start_value]

    for _ in range(50):
        change = random.randint(-10, 15)
        prices.append(prices[-1] + change)

    start_value = prices[-1]

    plt.figure(figsize=(8,4))
    plt.plot(prices, linewidth=2)
    plt.title("GISPI MARKET INDEX")
    plt.xlabel("Time")
    plt.ylabel("Index")
    plt.grid(True)

    filename = "gispi_chart.png"
    plt.savefig(filename)
    plt.close()

    await ctx.send(file=discord.File(filename))

if __name__ == "__main__":
    token = input("디스코드 봇 토큰을 입력하세요: ")
    bot.run(token)
