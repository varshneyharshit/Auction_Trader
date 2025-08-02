import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
if not TOKEN:
    print("Error: DISCORD_BOT_TOKEN environment variable is not set!")
    print("Please add your Discord bot token to the environment variables.")
    exit(1)

TARGET_CHANNEL_ID = 1401117679397502986  # Replace with your channel ID

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

def calculate_from_line(input_line):
    parts = input_line.strip().lower().split()
    ticket_type = parts[0]
    reward_counts = list(map(int, parts[1:]))

    if (
        ticket_type not in {'x1', 'x2', 'x3'}
        or len(reward_counts) != 7
        or reward_counts[0] not in [0, 1, 2]
    ):
        raise ValueError("Input must be like: 'x2 2 3 0 11 0 68 63'")

    value_map = {
        'x1': [270, 90, 45, 27, 9, 9, 6],
        'x2': [360, 180, 120, 90, 18, 18, 12],
        'x3': [540, 270, 180, 135, 27, 27, 18]
    }
    ticket_cost_map = {'x1': 1, 'x2': 2, 'x3': 3}

    values = value_map[ticket_type]
    ticket_cost = ticket_cost_map[ticket_type]

    input_tickets = sum(count * ticket_cost for count in reward_counts)
    total_points = sum(q * v for q, v in zip(reward_counts, values)) + values[0]
    output_tickets = total_points / 30
    ticket_loss = output_tickets - input_tickets
    loss_percent = (ticket_loss / input_tickets) * 100

    held_rewards = reward_counts[0] + 1
    held_points = held_rewards * values[0]
    sold_points = total_points - held_points

    net_point_loss = (input_tickets * 30) - sold_points
    total_gems = net_point_loss * 10 / held_rewards

    return {
        'input_tickets': input_tickets,
        'output_tickets': round(output_tickets, 2),
        'loss_percent': round(loss_percent, 2),
        'gem_cost_per_held_reward': total_gems,
        'held_rewards': held_rewards
    }

@bot.event
async def on_message(message):
    if message.author.bot or message.channel.id != TARGET_CHANNEL_ID or message.author == bot.user:
        return

    try:
        try:
            result = calculate_from_line(message.content)

            lines = []
            lines.append(
    "⚠️ **Don't include Last Prize as 1 in the input.**\n"
    "**It's automatically counted by default.**\n"
    "**If you include it manually, all calculations will be incorrect.**"
            )
            lines.append(f"**💸 Total Tickets Spent:** {result['input_tickets']}")
            lines.append(f"**🎟️ Tickets Received (If Everything Sold):** {result['output_tickets']}")

            lp = result['loss_percent']
            if lp > 0:
                lines.append(f"**📈 Trade Profit (If Everything Sold):** +{lp}%")
                lines.append("**💬 [You'll gain value with this trade, buy immediately]**")
            else:
                lines.append(f"**📉 Trade Loss (If Everything Sold):** {lp}%")

            gems_each = round(result['gem_cost_per_held_reward'])
            items_held = result['held_rewards']
            total_gems = int(round(gems_each * items_held))
            lines.append(f"**💎 Gem Cost:** {gems_each:,} gems each [{total_gems:,} total for {items_held} items]")

            await message.reply("\n".join(lines), mention_author=True)

        except ValueError:
            await message.reply(
                "⚠️ Invalid input format\n"
                "📝 Format: `x1/x2/x3` followed by 7 reward quantities [A–G]\n"
                "📌 Example: `x2 2 3 0 0 1 0 4`\n"
                "🚫 Do not skip any slots\n"
                "🟰 Use `0` if no rewards of that type available\n"
                "❌ Do not include the last prize",
                mention_author=True
            )

    except Exception as e:
        print(f"Unexpected error: {e}")
        await message.reply("❌ Unexpected error occurred.", mention_author=False)

bot.run(TOKEN)

