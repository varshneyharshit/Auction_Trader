Auction Trader Bot

A Discord bot that analyzes in-game auctions to help you maximize value and avoid bad deals. Input auction details, and the bot calculates ticket expenditure, profit/loss, and recommends whether to buy or skip. Ideal for gamers seeking automation and decision support.

***

## Features

- **Structured Auction Input:** Accepts auction details in a set format.
- **Computation:** Calculates total tickets spent, tickets received, and profit/loss percentage.
- **Gem Estimation:** Estimates gem cost per held item.
- **Actionable Recommendations:** Tells you when to buy or skip.
- **Instant Discord Replies:** Delivers results and tips right in your Discord channel.

***

## Input Format

```
x2/x3 <chest_size> <A> <B> <C> <D> <E> <F> <G>
```
- **x2** or **x3:** Ticket type
- **chest_size:** Chest capacity (80, 120, 160, 240)
- **A–G:** Quantities of each reward slot (7 total)

**Example:**
```
x2 240 2 3 0 0 1 0 4
```
- Do not include the last prize manually; it’s counted automatically.
- Use `0` for empty slots.
- All seven values required for accurate results.

***

## Requirements

- Python 3.10+
- `discord.py`
- `python-dotenv`

**Install dependencies:**
```sh
pip install discord.py python-dotenv
```

***

## Setup

1. **Create `.env` file** with your Discord bot token:
    ```
    DISCORD_BOT_TOKEN=your_token_here
    ```
2. **Set the `TARGET_CHANNEL_ID`** in the script to your chosen Discord channel.
3. **Run the bot:**
    ```sh
    python auction_trader_bot.py
    ```

***

## Usage

- Send auction input (as shown) in the bot’s designated channel.
- The bot replies with:
    - Total tickets spent
    - Tickets received if all sold
    - Profit/loss %
    - Gem cost per held reward
    - Recommendation to buy or skip

***

## Example Output

```
💸 Total Tickets Spent: 12
🎟️ Tickets Received (If Everything Sold): 13.2
📈 Trade Profit (If Everything Sold): +10%
💎 Gem Cost: 240 gems each [720 total for 3 items]
💬 [You'll gain value with this trade, buy immediately]
```

***

## Notes

- Do **not** list the last prize (it is auto-counted by the bot).
- Input `0` for empty reward slots.
- Great for displaying Python scripting, automation, Discord API proficiency, and creating value-driven gaming utilities.

***

## License

MIT

***

## Connect

- [My LinkedIn](https://in.linkedin.com/in/harshit-varshney-8348911ab)
- [My GitHub](https://github.com/varshneyharshit)

---

